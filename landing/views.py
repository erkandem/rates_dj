from django.views.generic import TemplateView


class LandPageView(TemplateView):
    template_name = 'static_pages/landing.html'
