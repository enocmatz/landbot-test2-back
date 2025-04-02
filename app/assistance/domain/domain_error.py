from typing import Type

class DomainError(Exception):
    def __init__(self, message='', status_code=400):
        self._message = message
        self._status_code = status_code

        super().__init__(self._message)

    def message(self):
        return self._message
    
    def get_status_code(self):
        return self._status_code;
    

class EntryNotFound(DomainError):
    def get_status_code(self):
        return 404

class InvalidTopicError(DomainError):
    def __init__(self, topic: str):
        self.topic = topic
        super().__init__(f"Invalid topic: {topic}", status_code=422)

class InvalidChannelError(DomainError):
    def __init__(self, channel: str):
        self.channel = channel
        super().__init__(f"Invalid channel: {channel}", status_code=422)

class NotNullError(DomainError):
    def __init__(self, field: str):
        self.field = field
        super().__init__(f"Field {field} cannot be null")

class NotEmptyError(DomainError):
    def __init__(self, field: str):
        self.field = field
        super().__init__(f"Field {field} cannot be empty", status_code=422)  