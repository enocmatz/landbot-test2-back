import pytest
from unittest.mock import Mock, patch

from app.assistance.domain.topic import Topic
from app.assistance.domain.assistance_request import AssistanceRequest
from app.assistance.infrastructure.emitters.slack_channel_emitter import SlackChannelEmitter
from app.assistance.infrastructure.clients.slack_client import SlackClient
from app.assistance.application.assistance_request_service import AssistanceRequestService
from app.assistance.application.channel_selector import ChannelSelector
from app.assistance.domain.domain_error import InvalidChannelError
from app.common.container import Container

class TestChannelSelector:
    def setup_method(self):
        self.email_channel_emitter = Container.email_channel_emitter()
        self.slack_channel_emitter = Container.slack_channel_emitter()

    @pytest.fixture
    def channel_selector(self,):
        return Container.channel_selector()

    def test_channel_selection_for_general_topic(self, channel_selector):
        topic = 'some_random_topic'

        with pytest.raises(InvalidChannelError):
            selected = channel_selector.select_channel(topic)

    def test_channel_selection_for_sales_topic(self, channel_selector):
        topic = Topic.SALES
        selected = channel_selector.select_channel(topic)
        assert selected == self.slack_channel_emitter

    def test_channel_selection_for_pricing_topic(self, channel_selector):
        topic = Topic.PRICING
        selected = channel_selector.select_channel(topic)
        assert selected == self.email_channel_emitter



