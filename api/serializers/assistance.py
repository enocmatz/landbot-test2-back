from rest_framework import serializers
from app.assistance.domain.assistance_request import AssistanceRequest
from app.assistance.domain.topic import Topic
from app.assistance.domain.domain_error import InvalidTopicError


class AssistanceSerializer(serializers.Serializer):
    topic = serializers.CharField(max_length=255, required=True)
    description = serializers.CharField(max_length=255, required=True)

    def to_domain_model(self):
        return AssistanceRequest(
            topic=self.validated_data['topic'],
            description=self.validated_data['description']
        )
    
    def validate_topic(self, value):
        Topic.validate_topic(value)
        return value