from django.urls import path
from app_1.consumers import EchoInfo


ws_urlpatterns = [
    path('ws/echo/', EchoInfo.as_asgi())
]
