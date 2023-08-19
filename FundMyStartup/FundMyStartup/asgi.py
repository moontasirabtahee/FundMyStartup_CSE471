"""
ASGI config for FundMyStartup project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FundMyStartup.settings')

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
import FundMyStartup.communication.routing
from channels.auth import AuthMiddlewareStack


application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            FundMyStartup.communication.routing.websocket_urlpatterns
        )
    )
})


application = ProtocolTypeRouter({
    'http': get_asgi_application(),
})
