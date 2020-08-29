from rest_framework.serializers import ModelSerializer

from .models import ECBRate


class ECBRateSerializer(ModelSerializer):
    class Meta:
        model = ECBRate
        fields = [
            "dt",
            "rate_3m",
            "rate_4m",
            "rate_6m",
            "rate_9m",
            "rate_1y",
            "rate_2y",
            "rate_5y",
            "rate_7y",
            "rate_10y",
            "rate_15y",
            "rate_30y",
        ]
