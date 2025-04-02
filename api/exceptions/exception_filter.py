from rest_framework.views import exception_handler
from rest_framework.response import Response
from app.common.errors.network_error import *
from app.assistance.domain.domain_error import *
from app.common.debug_utils import is_debug
import traceback

def custom_exception_filter(exc, context):
    response = None
    #Check if the exception is derived from DomainError
    if isinstance(exc, CoreNetworkError):
        response = Response({"message": exc.message()}, status=exc.get_status_code())
    elif isinstance(exc, DomainError    ):
        response = Response({"message": exc.message()}, status=exc.get_status_code())
    else:
        response = exception_handler(exc, context)
        if response is not None:
            response.data['status_code'] = response.status_code

    if response is None:
        print("No response from exception handler")
        response = Response({"message": "Internal server error"}, status=500)

    if is_debug():
        response.data['debug'] = {
            'type': type(exc).__name__,
            'traceback': traceback.format_exc().split('\n')
        }

    return response
