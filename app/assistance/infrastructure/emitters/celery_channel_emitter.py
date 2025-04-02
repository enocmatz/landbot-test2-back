from app.assistance.domain.channel_emitter import ChannelEmitter
from app.assistance.domain.assistance_request import AssistanceRequest
import logging

logger = logging.getLogger(__name__)

def emit_request(emitter: ChannelEmitter, request: AssistanceRequest):
    emitter.emit(request)

class CeleryChannelEmitterDecorator(ChannelEmitter):
    def __init__(self, emitter: ChannelEmitter):
        self._instance = emitter 
        self.logger = logging.getLogger(__name__)

    def emit(self, request: AssistanceRequest):
        self.logger.info("Task is deferred to celery")
        emit_request(self._instance, request)
        return True 