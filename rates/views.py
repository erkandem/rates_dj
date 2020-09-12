from django.db.models import QuerySet
from rest_framework.generics import ListAPIView

from .models import ECBRate
from .serializers import (
    ECBRateSerializer,
    ECBRateSerializerFieldNameValidation,
)


class EcbRatesView(
    ListAPIView,
):
    """
    Get the time series for the entire yield curve
    """
    serializer_class = ECBRateSerializer

    def get_queryset(self) -> QuerySet:
        return ECBRate.objects.all().order_by('-dt')


class EcbRatesSingleView(
    ECBRateSerializerFieldNameValidation,
    ListAPIView,
):
    """
    Get time series for a single duration (e.g. 1y rate)
    """
    serializer_class = ECBRateSerializer

    def get_queryset(self) -> QuerySet:
        return ECBRate.objects.all().order_by('-dt')
