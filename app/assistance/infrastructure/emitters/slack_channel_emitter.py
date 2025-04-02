from app.assistance.domain.channel_emitter import ChannelEmitter
from app.assistance.domain.assistance_request import AssistanceRequest
from app.assistance.infrastructure.clients.slack_client import SlackClient
import logging

class SlackChannelEmitter(ChannelEmitter):
    def __init__(self, client: SlackClient):
        self.logger = logging.getLogger(__name__)
        self.client = client

    def emit(self, assistance_request: AssistanceRequest):
        self.logger.info(f"Emitting assistance request to Slack: {assistance_request}")
        return self.client.send_message(channel='#cosas', message=f"New assistance request: {assistance_request}")
