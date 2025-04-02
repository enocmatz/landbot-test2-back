from enum import Enum
from app.assistance.domain.domain_error import InvalidTopicError

class Topic(str, Enum):
    SALES = "sales"
    PRICING = "pricing"

    def validate_topic(value):
        if value not in Topic.__members__.values():
            raise InvalidTopicError(f"Invalid topic: {value}")
        return value