# import os
# from django.core.asgi import get_asgi_application
# from channels.routing import ProtocolTypeRouter, URLRouter
# from chat.routing import websocket_urlpatterns  # Import the WebSocket URL patterns from your app

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     "websocket": URLRouter(websocket_urlpatterns),  # Use the imported WebSocket URL patterns
# })
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

from chat import routing  # Import your app's routing
# from inbox import routing
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_name.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket":
        URLRouter(
            routing.websocket_urlpatterns
        )
    
})