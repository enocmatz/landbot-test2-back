from app.assistance.domain.assistance_request import AssistanceRequest
from app.assistance.application.channel_selector import ChannelSelector
from app.assistance.domain.domain_error import NotNullError

class AssistanceRequestService:
    def __init__(self, channel_selector: ChannelSelector):
        self.channel_selector = channel_selector
    
    def handle(self, assistance_request: AssistanceRequest):
        if assistance_request is None:
            raise NotNullError("assistance_request")    
        
        channel_emitter = self.channel_selector.select_channel(assistance_request.topic())
        channel_emitter.emit(assistance_request)
        return "Request sent"
