import json

# Odoo modules
from odoo.http import Response

# __appResponse
# NOTE: DO NOT USE THIS METHOD FROM OUTSIDE THIS MODULE
def __appResponse(success: bool, statusCode: int, message: str, data, errors: dict = None) -> Response:
        dictData = {'success': success}

        if message:
            dictData['message'] = message

        if data:
            dictData['data'] = data

        if errors:
            dictData['errors'] = errors

        return Response(
            json.dumps(dictData),
            status = statusCode,
        )

# __appResponse

# SuccessResponse
def SuccessResponse(data, message: str = None, statusCode: int = 200):
    return __appResponse(True, statusCode, message, data)

# SuccessResponse

# ErrorResponse
def ErrorResponse(errors: dict = None, message: str = 'Some error has occurred.', statusCode: int = 500):
    return __appResponse(False, statusCode, message, None, errors)

# ErrorResponse

# InvalidDataResponse
def InvalidDataResponse(errors: dict = None, message: str = 'There are some invalid data found. Please correct them all to continue.', statusCode: int = 400):
    return __appResponse(False, statusCode, message, None, errors)

# InvalidDataResponse

# NotFoundResponse
def NotFoundResponse(message: str = 'Not found.'):
    return __appResponse(False, 404, message, None, None)

# NotFoundResponse

# UnauthorizedResponse
def UnauthorizedResponse(message: str = 'You do not have sufficient permission to proceed.'):
    return __appResponse(False, 401, message, None, None)

# UnauthorizedResponse