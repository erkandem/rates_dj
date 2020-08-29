from rest_framework.viewsets import ModelViewSet

from .models import ECBRate
from .serializers import ECBRateSerializer


class EcbRatesView(ModelViewSet):
    """
    Additional filtering might be added with this:
    https://www.django-rest-framework.org/api-guide/filtering/
    """

    queryset = ECBRate.objects.all()
    serializer_class = ECBRateSerializer
