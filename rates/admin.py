from django.contrib import admin

from .models import ECBRate


@admin.register(ECBRate)
class ECBRatesAdmin(admin.ModelAdmin):
    pass
