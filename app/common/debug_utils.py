import os

def is_debug():
    return os.getenv('DEBUG', 'True').lower() == 'true'