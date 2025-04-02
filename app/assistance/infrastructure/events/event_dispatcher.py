from app.assistance.application.interfaces.event_dispatcher import EventDispatcher
from app.assistance.domain.events.assistance_request_events import AssistanceRequestCreatedEvent

class RealEventDispatcher(EventDispatcher):
    def dispatch(self, event: Any) -> None:
        if isinstance(event, AssistanceRequestCreatedEvent):
            # Here you could:
            # - Send to message queue
            # - Notify other services
            # - Trigger webhooks
            # - Log the event
            # - etc.
            print(f"Dispatching event: {event}") 