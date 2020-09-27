from datetime import date
from datetime import datetime as dt
import typing

from django.db.models import QuerySet
from rest_framework.exceptions import ParseError
from rest_framework.generics import ListAPIView

from .models import ECBRate
from .serializers import (
    ECBRateSerializer,
    ECBRateSerializerFieldNameValidation,
)


class StartAndEndDateFilterMixin:

    @staticmethod
    def validate_date(
            date_to_parse: typing.Union[str, None],
            param_name: str
    ) -> typing.Union[date, None]:
        """
        attempt, to parse a date with raising an helpful error message
        Args:
            date_to_parse: ISO str representation of an date
            param_name: keyword of date_to_parse

        Returns:
            None
            datetime.date

        Raises:
            rest_framework.exceptions.ParseError
        """
        if date_to_parse is not None:
            try:
                parsed_date = dt.strptime(date_to_parse, '%Y-%m-%d').date()
            except ValueError:
                raise ParseError(
                    f'`{param_name}` is supposed to be the ISO date format e.g. 1999-12-24'
                )
            return parsed_date
        else:
            return None

    @staticmethod
    def validate_date_config(
            start_date: date,
            end_date: date
    ) -> None:
        """
        checks that one date is earlier than the second one.

        Raises:
            rest_framework.exceptions.ParseError

        """
        if start_date > end_date:
            raise ParseError(
                f'start date ({str(start_date)}) has to be earlier than end date ({str(end_date)})'
            )

    def filter_queryset_by_date(
            self,
            queryset: QuerySet
    ) -> QuerySet:
        """
        limit the size of the queryset by filtering by date
        if they are available in context of a request.

        Args:
            queryset: unfiltered queryset if the view

        Returns:
            queryset - same as input but filtered by date
        """
        start_date = self.request.query_params.get('startDate', None)
        if start_date:
            start_date = self.validate_date(start_date, 'startDate')
        end_date = self.request.query_params.get('endDate', None)
        if end_date:
            end_date = self.validate_date(end_date, 'endDate')
        if start_date and not end_date:
            queryset = queryset.filter(dt__gte=start_date)
        elif not start_date and end_date:
            queryset = queryset.filter(dt__lte=end_date)
        elif start_date and end_date:
            self.validate_date_config(start_date, end_date)
            queryset = queryset.filter(dt__range=(start_date, end_date,))
        return queryset


class EcbRatesView(
    StartAndEndDateFilterMixin,
    ListAPIView,
):
    """
    Get the time series for the entire yield curve
    """
    serializer_class = ECBRateSerializer

    def get_queryset(self) -> QuerySet:
        queryset = ECBRate.objects.all().order_by('-dt')
        return self.filter_queryset_by_date(queryset)


class EcbRatesSingleView(
    StartAndEndDateFilterMixin,
    ECBRateSerializerFieldNameValidation,
    ListAPIView,
):
    """
    Get time series for a single duration (e.g. 1y rate)
    """
    serializer_class = ECBRateSerializer

    def get_queryset(self) -> QuerySet:
        queryset = ECBRate.objects.all().order_by('-dt')
        return self.filter_queryset_by_date(queryset)
