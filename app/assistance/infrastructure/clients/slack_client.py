from slack_sdk import WebClient
from urllib.error import URLError
from app.common.errors.network_error import NetworkError, UnknownNetworkError
from app.common.debug_utils import is_debug

import logging


class SlackClient:
    def __init__(self, token: str):
        self.logger = logging.getLogger(__name__)
        self.slack_client = WebClient(token=token)

        if is_debug():
            self.slack_client.logger.setLevel(logging.DEBUG)
        else:
            self.slack_client.logger.setLevel(logging.INFO)

    def send_message(self, channel: str, message: str):
        try:
            response = self.slack_client.chat_postMessage(channel=channel, text=message)
            return response['ok']
        except URLError as e:
            raise NetworkError(e)
        except Exception as e:
            raise UnknownNetworkError(e)
        except:
            raise UnknownNetworkError('Something wrong')
        return False
