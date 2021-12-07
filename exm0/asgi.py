"""
ASGI config for exm0 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'exm0.settings')
from django.core.asgi import get_asgi_application
from app_1.routing import ws_urlpatterns

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack


application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            ws_urlpatterns
        )
    )
})

