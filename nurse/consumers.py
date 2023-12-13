# consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer

class PatientEntryConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("patient_entries_updates", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("patient_entries_updates", self.channel_name)

    async def patient_entry_update(self, event):
        data = event["data"]
        await self.send(text_data=json.dumps(data))
