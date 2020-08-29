from django.conf.urls import (
    include,
    url,
)
from rest_framework.routers import SimpleRouter

from .views import EcbRatesView

router = SimpleRouter()
router.register("ecb", EcbRatesView, basename="ecbrates")

urlpatterns = [url(r"^", include(router.urls))]
