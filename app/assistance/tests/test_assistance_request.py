import pytest
from app.assistance.domain.assistance_request import AssistanceRequest
from app.assistance.domain.domain_error import NotNullError, NotEmptyError
from app.assistance.domain.topic import Topic

class TestAssistanceRequest:

    def test_assistance_request_should_raise_error_if_topic_is_none(self):
        with pytest.raises(NotNullError):
            AssistanceRequest(None, "test")

    def test_assistance_request_should_raise_error_if_description_is_none(self):
        with pytest.raises(NotNullError):
            AssistanceRequest(Topic.SALES, None)

    def test_assistance_request_should_create_request_with_valid_topic_and_description(self):
        request = AssistanceRequest(Topic.SALES, "test")
        assert request.topic() == Topic.SALES
        assert request.description() == "test"

    def test_assistance_request_should_raise_error_if_topic_is_empty(self):
        with pytest.raises(NotEmptyError):
            AssistanceRequest("", "test")

    def test_assistance_request_should_raise_error_if_description_is_empty(self):
        with pytest.raises(NotEmptyError):
            AssistanceRequest(Topic.SALES, "")