from django.contrib import admin
from app.base.models import Settings, SettingsIndexPage, Banner
# Register your models here.
admin.site.register(Settings)
admin.site.register(SettingsIndexPage)
admin.site.register(Banner)
