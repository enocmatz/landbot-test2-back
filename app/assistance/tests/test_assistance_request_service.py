import pytest
from unittest.mock import Mock
from app.common.container import Container
from app.assistance.domain.topic import Topic
from app.assistance.domain.assistance_request import AssistanceRequest
from app.assistance.application.channel_selector import ChannelSelector
from app.assistance.domain.channel_emitter import ChannelEmitter
from app.assistance.domain.domain_error import NotNullError

class TestAssistanceRequestService:
    @pytest.fixture
    def mock_emitter(self):
        return Mock(spec=ChannelEmitter)

    @pytest.fixture
    def mock_channel_selector(self, mock_emitter):
        mock = Mock(spec=ChannelSelector)
        mock.select_channel.return_value = mock_emitter
        return mock
    
    @pytest.fixture
    def assistance_request_service(self, mock_channel_selector):
        return Container.assistance_request_service(channel_selector=mock_channel_selector)

    def test_assistance_request_service_should_raise_error_if_request_is_none(self, assistance_request_service, mock_emitter):
        prev_channel_selector_call_count = assistance_request_service.channel_selector.select_channel.call_count
        prev_emitter_call_count = mock_emitter.emit.call_count

        with pytest.raises(NotNullError):
            assistance_request_service.handle(None)

        #Should not select channel
        assert assistance_request_service.channel_selector.select_channel.call_count == prev_channel_selector_call_count
        #Should not emit request
        assert mock_emitter.emit.call_count == prev_emitter_call_count

    def test_assistance_request_service_should_emit_request(self, assistance_request_service, mock_emitter):
        prev_channel_selector_call_count = assistance_request_service.channel_selector.select_channel.call_count
        prev_emitter_call_count = mock_emitter.emit.call_count

        req = AssistanceRequest(Topic.SALES, "Hello, how are you?")
        assistance_request_service.handle(req)
        
        #Should select channel once 
        assert assistance_request_service.channel_selector.select_channel.call_count == prev_channel_selector_call_count + 1
        #Should emit request once
        assert mock_emitter.emit.call_count == prev_emitter_call_count + 1
