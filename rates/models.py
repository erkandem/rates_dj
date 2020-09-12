from django.db import models


class ECBRateDetailsMixin:
    """
    container to include string literals, keys, mappings and
    frequently used groupings thereof
    """
    ECB_RATE_PK = 'dt'
    ECB_RATE_3M = "rate_3m"
    ECB_RATE_4M = "rate_4m"
    ECB_RATE_6M = "rate_6m"
    ECB_RATE_9M = "rate_9m"
    ECB_RATE_1Y = "rate_1y"
    ECB_RATE_2Y = "rate_2y"
    ECB_RATE_5Y = "rate_5y"
    ECB_RATE_7Y = "rate_7y"
    ECB_RATE_10Y = "rate_10y"
    ECB_RATE_15Y = "rate_15y"
    ECB_RATE_30Y = "rate_30y"
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
    ECB_RATE_FIELDS = [ECB_RATE_PK] + ECB_RATE_KEYS

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


class ECBRate(
    ECBRateDetailsMixin,
    models.Model
):
    """
    Model interact with ECB risk free rate data
    """

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
