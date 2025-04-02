from app.assistance.domain.topic import Topic
from app.assistance.infrastructure.emitters.slack_channel_emitter import SlackChannelEmitter
from app.assistance.infrastructure.emitters.email_channel_emitter import EmailChannelEmitter
from app.assistance.domain.channel_emitter import ChannelEmitter
from app.assistance.infrastructure.clients.slack_client import SlackClient
from app.assistance.domain.domain_error import InvalidChannelError
from typing import Callable
import logging

class ChannelSelector:

    def __init__(self, channel_mapping: dict[Topic, Callable[..., ChannelEmitter]]):
        self.channel_mapping = channel_mapping
        self.logger = logging.getLogger(__name__)

    def select_channel(self, topic: Topic) -> ChannelEmitter:
        if topic not in self.channel_mapping:
            self.logger.error(f"No channel found for topic: {topic}")
            raise InvalidChannelError(topic);
        
        return self.channel_mapping[topic]
