import json
import logging

from channels.generic.websocket import WebsocketConsumer

logger = logging.getLogger('django')

class ChatComsumer(WebsocketConsumer):
    def connect(self):
        self.name = self.scope['url_route']['kwargs']['name']
        self.accept()
        logger.debug('connect')

    def disconnect(self, close_code):
        logger.debug('disconnect')

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = self.name + ': ' + text_data_json['message']
        logger.debug('send')
        
        self.send(text_data=json.dumps({
            'message': message
        }))

