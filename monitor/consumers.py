# chat/consumers.py
from channels.generic.websocket import  AsyncWebsocketConsumer
import json
from time import gmtime, strftime, sleep
class MonitorConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
    async def disconnect(self, close_code):
        pass
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['type']
        user = self.scope['user']
        message = text_data
        await self.send(text_data=json.dumps({
            'message': message
        }))
