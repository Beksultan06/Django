from django.shortcuts import render
from app.base.models import SettingsIndexPage, Banner

def index(requets):
    settings_id = SettingsIndexPage.objects.latest("id")
    banner_all = Banner.objects.all()
    return render(requets, 'base/index.html', locals())