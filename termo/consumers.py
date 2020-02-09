from channels.generic.websocket import AsyncWebsocketConsumer


class CurrentConsumer(AsyncWebsocketConsumer):
    groups = ["termo"]

    async def connect(self):
        # Called on connection.
        # To accept the connection call:
        await self.accept()
        await self.send(text_data='Hello consumer')

    async def receive(self, text_data=None, bytes_data=None):
        # Called with either text_data or bytes_data for each frame
        # You can call:
        await self.send(text_data="Hello world!")
        # Or, to send a binary frame:
        await self.send(bytes_data="Hello world!")
        # Want to force-close the connection? Call:
        await self.close()
        # Or add a custom WebSocket error code!
        await self.close(code=4123)

    async def send_current(self):
        await self.send(text_data="some currend data")

    async def disconnect(self, close_code):
        # Called when the socket closes
        pass
