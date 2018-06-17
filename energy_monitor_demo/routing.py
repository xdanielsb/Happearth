from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import monitor.routing
application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            monitor.routing.websocket_urlpatterns
        )
    ),
})
