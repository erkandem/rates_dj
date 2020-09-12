from django.conf.urls import url

from .views import (
    EcbRatesSingleView,
    EcbRatesView,
)

urlpatterns = [
    url(r"ecb/$", EcbRatesView.as_view(), name="api-ecbrates"),
    url(r"ecb/(?P<rate_duration>\w+)/$", EcbRatesSingleView.as_view(), name="api-ecbrates-single"),
]
