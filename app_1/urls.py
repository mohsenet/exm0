from django.conf.urls import url
from app_1.views import index


urlpatterns = [
    url(r'^$', index, name='index'),
]
