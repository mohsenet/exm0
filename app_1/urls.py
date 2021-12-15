from django.conf.urls import url
from app_1.views import index, progressbar


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^progressbar$', progressbar, name='progressbar'),
]
