from app.assistance.domain.topic import Topic 
from app.assistance.domain.domain_error import NotNullError, NotEmptyError
from uuid import UUID, uuid4
from typing import List

class AssistanceRequest: 
    def __init__(self, topic: Topic, description: str, id: UUID = None):
        if topic is None:
            raise NotNullError("topic")
        if description is None:
            raise NotNullError("description")
        
        if len(description) == 0:
            raise NotEmptyError("description")
        
        if len(topic) == 0:
            raise NotEmptyError("topic")
        
        self._id = id if id is not None else uuid4()
        self._topic = topic 
        self._description = description


    
    def id(self) -> UUID:
        return self._id

    def topic(self) -> Topic:
        return self._topic
    
    def description(self) -> str:
        return self._description
    
    def __str__(self) -> str:
        return f"ID: {self._id}, Topic: {self._topic}, Description: {self._description}"
