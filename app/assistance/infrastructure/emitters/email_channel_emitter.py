from app.assistance.domain.channel_emitter import ChannelEmitter
from app.assistance.domain.assistance_request import AssistanceRequest
import logging

class EmailChannelEmitter(ChannelEmitter):
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def emit(self, assistance_request: AssistanceRequest):
        self.logger.info(f"Emitting assistance request to Email: {assistance_request}")
        return True