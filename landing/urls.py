from django.conf.urls import url

from .views import LandPageView

urlpatterns = [
    url(r"^$", LandPageView.as_view(), name="landing-page"),
]
