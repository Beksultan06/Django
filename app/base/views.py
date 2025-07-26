from django.shortcuts import render
from app.base.models import SettingsIndexPage, Banner, About, Visa

def index(requets):
    settings_id = SettingsIndexPage.objects.latest("id")
    banner_all = Banner.objects.all()
    about_all = About.objects.all()
    visa_all = Visa.objects.all()
    return render(requets, 'base/index.html', locals())

def about(request):
    return render(request, "base/about-us.html", locals())

def contact(request):
    return render(request, 'base/contact-us.html', locals())