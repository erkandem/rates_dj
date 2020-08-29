from datetime import date

from django.db import models
import factory


class ECBRateDetailsMixin:
    ECB_RATE_3M = "ECB_3M"
    ECB_RATE_4M = "ECB_4M"
    ECB_RATE_6M = "ECB_6M"
    ECB_RATE_9M = "ECB_9M"
    ECB_RATE_1Y = "ECB_1Y"
    ECB_RATE_2Y = "ECB_2Y"
    ECB_RATE_5Y = "ECB_5Y"
    ECB_RATE_7Y = "ECB_7Y"
    ECB_RATE_10Y = "ECB_10Y"
    ECB_RATE_15Y = "ECB_15Y"
    ECB_RATE_30Y = "ECB_30Y"

    ECB_RATE_KEYS = [
        ECB_RATE_3M,
        ECB_RATE_4M,
        ECB_RATE_6M,
        ECB_RATE_9M,
        ECB_RATE_1Y,
        ECB_RATE_2Y,
        ECB_RATE_5Y,
        ECB_RATE_7Y,
        ECB_RATE_10Y,
        ECB_RATE_15Y,
        ECB_RATE_30Y,
    ]

    ECB_RATES_ECB_WAREHOUSE_MAPPING = {
        ECB_RATE_3M: "YC/B.U2.EUR.4F.G_N_A.SV_C_YM.PY_3M",
        ECB_RATE_4M: "YC/B.U2.EUR.4F.G_N_A.SV_C_YM.PY_4M",
        ECB_RATE_6M: "YC/B.U2.EUR.4F.G_N_A.SV_C_YM.PY_6M",
        ECB_RATE_9M: "YC/B.U2.EUR.4F.G_N_A.SV_C_YM.PY_9M",
        ECB_RATE_1Y: "YC/B.U2.EUR.4F.G_N_A.SV_C_YM.PY_1Y",
        ECB_RATE_2Y: "YC/B.U2.EUR.4F.G_N_A.SV_C_YM.PY_2Y",
        ECB_RATE_5Y: "YC/B.U2.EUR.4F.G_N_A.SV_C_YM.PY_5Y",
        ECB_RATE_7Y: "YC/B.U2.EUR.4F.G_N_A.SV_C_YM.PY_7Y",
        ECB_RATE_10Y: "YC/B.U2.EUR.4F.G_N_A.SV_C_YM.PY_10Y",
        ECB_RATE_15Y: "YC/B.U2.EUR.4F.G_N_A.SV_C_YM.PY_15Y",
        ECB_RATE_30Y: "YC/B.U2.EUR.4F.G_N_A.SV_C_YM.PY_30Y",
    }

    ECB_RATES_DURATION_YEARS_MAPPING = {
        ECB_RATE_3M: 3 / 12,
        ECB_RATE_4M: 4 / 12,
        ECB_RATE_6M: 6 / 12,
        ECB_RATE_9M: 9 / 12,
        ECB_RATE_1Y: 1,
        ECB_RATE_2Y: 2,
        ECB_RATE_5Y: 5,
        ECB_RATE_7Y: 7,
        ECB_RATE_10Y: 10,
        ECB_RATE_15Y: 15,
        ECB_RATE_30Y: 30,
    }


class ECBRate(ECBRateDetailsMixin, models.Model):

    dt = models.DateField(primary_key=True)
    rate_3m = models.FloatField()
    rate_4m = models.FloatField()
    rate_6m = models.FloatField()
    rate_9m = models.FloatField()
    rate_1y = models.FloatField()
    rate_2y = models.FloatField()
    rate_5y = models.FloatField()
    rate_7y = models.FloatField()
    rate_10y = models.FloatField()
    rate_15y = models.FloatField()
    rate_30y = models.FloatField()


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
