from abc import ABC, abstractmethod
from app.assistance.domain.assistance_request import AssistanceRequest

class ChannelEmitter(ABC):
    @abstractmethod
    def emit(self, assistance_request: AssistanceRequest) -> bool:
        pass
