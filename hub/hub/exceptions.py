from rest_framework.exceptions import ValidationError,APIException
from rest_framework.response import Response
from rest_framework.views import exception_handler
import logging


logger=logging.getLogger(__name__)


class BaseException(APIException):
    def __init__(self,
                 detail=None,
                 response_code=None,
                 error_code=None):
        self.detail = detail
        self.response_code = response_code
        self.error_code = error_code
        

class GenericFieldException(BaseException):
    status_code=400
    default_code=400
    default_detail=(
        "A field exception was encountered"
        )
    
class ServerFaultException(BaseException):
    status_code=500
    default_code=500
    default_detail=(
        "Server exception was encountered.Please try again later."
    )


def custom_exception_handler(exception:Exception,context):
    status_code=500
    code=500
    details="Some unexpected error occurred"
    
    if isinstance(exception,BaseException):
        status_code=exception.status_code or exception.response_code
        code=exception.error_code or exception.default_code
        details=exception.detail or exception.default_detail
        
    else:
        response=exception_handler(exception, context)
        if isinstance(exception, ValidationError):
            code = GenericFieldException.default_code
            details = GenericFieldException.default_detail
        elif response is None or response.status_code == 500:
            code = ServerFaultException.default_code
            details = ServerFaultException.default_detail
            logger.exception(exception)
        if response:
            response.data["errorCode"] = code
            response.data["errorMsg"] = details
            return response

    data = {
        "status_code": status_code,
        "errorCode": code,
        "errorMsg": details,
    }
    return Response(data, status=status_code)
