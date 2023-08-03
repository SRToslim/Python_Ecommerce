from django.contrib import admin

from web_settings.models import Currency


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ['name', 'symbol', 'is_active']


admin.site.register(Currency, CurrencyAdmin)
