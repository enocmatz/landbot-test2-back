
class CoreNetworkError(Exception):
    def __init__(self, message='', status_code=500):
        self._message = message
        self._status_code = status_code
        super().__init__(self._message)

    def message(self):
        return self._message
    
    def get_status_code(self):
        return self._status_code
    

class NetworkError(CoreNetworkError):
    def __init__(self, error):
        self.error = error
        super().__init__(f"Network error: {error}")

class UnknownNetworkError(CoreNetworkError):
    def __init__(self, error):
        self.error = error
        super().__init__(f"Unknown network error: {error}") 

class MaxFailsReached(CoreNetworkError):
    def __init__(self, retries): 
        super().__init__(f"Task failed after {retries} retries.", status_code=503)