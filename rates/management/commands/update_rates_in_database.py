from argparse import ArgumentParser
from datetime import date
from datetime import datetime as dt
from datetime import timedelta
import json
import typing as t

import certifi
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError
import urllib3

from rates.models import ECBRate


def rfr_eu(
        start_date: date,
        end_date: date
) -> t.Dict[str, t.Dict[date, float]]:
    """
    Queries the ECB data ware house via http requests for Euro area risk free rates and
    returns the parsed JSON. Only core data is returned.

    Examples:

        import pprint
        import datetime
        rfr_eu(datetime.date(2019, 1, 1), datetime.date(2019, 1, 2))
        pprint.pprint(data)
        {'YC/B.U2.EUR.4F.G_N_A.SV_C_YM.PY_10Y': {datetime.date(2019, 1, 2): 0.22376075696834297},
         'YC/B.U2.EUR.4F.G_N_A.SV_C_YM.PY_15Y': {datetime.date(2019, 1, 2): 0.5216230211127632},
         'YC/B.U2.EUR.4F.G_N_A.SV_C_YM.PY_1Y': {datetime.date(2019, 1, 2): -0.6882995030932628},
         'YC/B.U2.EUR.4F.G_N_A.SV_C_YM.PY_2Y': {datetime.date(2019, 1, 2): -0.6694237299164698},
         'YC/B.U2.EUR.4F.G_N_A.SV_C_YM.PY_30Y': {datetime.date(2019, 1, 2): 0.8425236263062917},
         'YC/B.U2.EUR.4F.G_N_A.SV_C_YM.PY_3M': {datetime.date(2019, 1, 2): -0.6268384098292605},
         'YC/B.U2.EUR.4F.G_N_A.SV_C_YM.PY_4M': {datetime.date(2019, 1, 2): -0.6378545182410699},
         'YC/B.U2.EUR.4F.G_N_A.SV_C_YM.PY_5Y': {datetime.date(2019, 1, 2): -0.3281012687616979},
         'YC/B.U2.EUR.4F.G_N_A.SV_C_YM.PY_6M': {datetime.date(2019, 1, 2): -0.6564968619685326},
         'YC/B.U2.EUR.4F.G_N_A.SV_C_YM.PY_7Y': {datetime.date(2019, 1, 2): -0.07405599742948608},
         'YC/B.U2.EUR.4F.G_N_A.SV_C_YM.PY_9M': {datetime.date(2019, 1, 2): -0.6766213935721408}}

    Args:
        start_date: result begins and including the ``start_date``
        end_date: result upto and including the ``end_date``

    Returns:

    """
    CONTENT_HEADER = {'Accept': 'application/vnd.sdmx.data+json;version=1.0.0-wd'}
    POOL = urllib3.PoolManager(
        cert_reqs='CERT_REQUIRED',
        ca_certs=certifi.where(),
    )
    BASE_URL = 'https://sdw-wsrest.ecb.europa.eu/service/data/'
    if start_date > end_date:
        raise ValueError('The `start_date` is supposed to be earlier than `end_date`')
    params = {
        'startPeriod': start_date.strftime('%Y-%m-%d'),
        'endPeriod': end_date.strftime('%Y-%m-%d'),
    }
    results = {}
    for k, dataset_name in enumerate(ECBRate.ECB_RATES_ECB_WAREHOUSE_MAPPING.values()):
        final_url = f'{BASE_URL}{dataset_name}'
        response = POOL.request(
            method='GET',
            url=final_url,
            fields=params,
            headers=CONTENT_HEADER
        )
        if response.status == 200:
            data = json.loads(response.data.decode('utf-8'))
            observations = data['dataSets'][0]['series']['0:0:0:0:0:0:0']['observations']
            observation_dates = data['structure']['dimensions']['observation'][0]['values']
            results[dataset_name] = {
                dt.strptime(date_['id'], '%Y-%m-%d').date(): rate_[0]
                for date_, rate_ in zip(observation_dates, observations.values())
            }
        else:
            print(f'Had trouble with an URL. Status: {response.status} URL: {final_url}')
    return results


def ecb_update(
        start_date: date = None,
        end_date: date = None,
        delta_days: int = None,
) -> None:
    """
    Will query ECB data ware house for the yield curve
    for a given ``start_date`` and ``end_date``.
    If no dates are given a default of 5 days are queried and
    inserted to the database.

    TODO: Each object is inserted individually to catch ``IntegrityError``.
          It would be much fast with ``ECBRate.objects.bulk_create``
          How do you handle collisions during bulk operations ?

    Args:
        start_date: begins here and result includes the ``start_date``
        end_date: begins here and  result includes the ``end_date``
        delta_days: number of days going back default 5

    """
    print(f'{dt.now()} starting update')
    if delta_days is None:
        delta_days = 5
    if start_date is None:
        start_date = date.today() - timedelta(days=delta_days)
    if end_date is None:
        end_date = date.today()
    new_records = rfr_eu(start_date, end_date)
    ecb_rate_data = [{'dt': date_} for date_ in new_records[list(new_records.keys())[0]].keys()]
    for k, record in enumerate(ecb_rate_data):
        ecb_rate_data[k].update({
            db_field: new_records[api_field][record['dt']]
            for db_field, api_field in ECBRate.ECB_RATES_ECB_WAREHOUSE_MAPPING.items()
        })
    ecb_rate_objects = [ECBRate(**record) for record in ecb_rate_data]
    for ecb_rate_object in ecb_rate_objects:
        try:
            ecb_rate_object.save()
            print(f'{str(ecb_rate_object.dt)} saved')
        except IntegrityError:
            print(f'{str(ecb_rate_object.dt)} already in database')


def get_date_intervals(
        start_date: date,
        years: int
) -> t.Tuple[t.List[date], t.List[date]]:
    end_dates = [
        date(start_date.year + year, 1, 1) - timedelta(days=1)
        for year in range(1, years, 1)
    ]
    start_dates = [
        date(start_date.year + year - 1, 1, 1)
        for year in range(1, years, 1)
    ]
    start_dates[0] = start_date
    return start_dates, end_dates


def ecb_initial(start_date: date = None):
    """
    Initial data acquisition.
    Will query the ECB data ware house in chunks of 1 year and
    insert the result into the database using ``ecb_update``.
    """
    print(f'{dt.now()} starting getting initial data')
    if not start_date:
        start_date = date(2004, 1, 1)
    years = date.today().year - start_date.year + 2  # include the limits
    start_dates, end_dates = get_date_intervals(start_date, years)
    for chunk_start, chunk_end in zip(start_dates, end_dates):
        print(f'loading data from {str(chunk_start)} until {str(chunk_end)}')
        ecb_update(chunk_start, chunk_end)


class Command(BaseCommand):
    help = "Load rates since 2014 into the database"
    UPDATE_MODE = "update"
    INITIAL_MODE = "initial"

    def add_arguments(self, parser: ArgumentParser) -> ArgumentParser:
        parser.add_argument(
            'mode',
            type=str,
            choices=[self.UPDATE_MODE, self.INITIAL_MODE],
            default=self.UPDATE_MODE
        )
        parser.add_argument(
            '--update_delta_days',
            default=None,
            type=int,
        )
        parser.add_argument(
            '--start_date',
            default=None,
            type=date,
        )
        parser.add_argument(
            '--end_date',
            default=None,
            type=date,
        )
        return parser

    def handle(self, *args: t.Any, **options: t.Any):
        if options['mode'] == self.UPDATE_MODE:
            ecb_update(
                start_date=options['start_date'],
                end_date=options['end_date'],
                delta_days=options['update_delta_days'],
            )
        elif options['mode'] == self.INITIAL_MODE:
            ecb_initial(
                start_date=options['start_date'],
            )
        print(f'{dt.now()} exiting management command')
