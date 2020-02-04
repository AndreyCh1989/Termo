from channels.routing import URLRouter, ProtocolTypeRouter
from django.conf.urls import url

from termo.consumers import CurrentConsumer

websockets = URLRouter([
    url(r"^ws/current/$", CurrentConsumer, name="current"),
])

application = ProtocolTypeRouter({
    "websocket": websockets,
})
