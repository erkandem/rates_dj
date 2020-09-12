from datetime import date

import factory

from rates.models import ECBRate


class ECBRateFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ECBRate

    dt = date(2019, 1, 1)
    rate_3m = 0.01
    rate_4m = 0.01
    rate_6m = 0.01
    rate_9m = 0.01
    rate_1y = 0.01
    rate_2y = 0.01
    rate_5y = 0.01
    rate_7y = 0.01
    rate_10y = 0.01
    rate_15y = 0.01
    rate_30y = 0.01
