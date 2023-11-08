from typing import Final
import json
from datetime import datetime

# Odoo modules
from odoo import http
from odoo.http import request, Response

# Custom modules
from odoo.addons.pro_hrms.helpers import sessionHelper, jwtHelper, moduleResponse
from odoo.addons.pro_hrms.helpers.moduleResponse import UnauthorizedResponse, ErrorResponse

# BaseController
class BaseController(http.Controller):
    __MODULE_URL_PREFIX: Final = '/hrms/api'

    # moduleRoute
    @staticmethod
    def moduleRoute(url, method, auth):
        # Format module API URL
        if not url.startswith('/'):
            url = BaseController.__MODULE_URL_PREFIX + '/' + url

        def wrapper(func):
            @http.route([url], type = 'json', auth = 'public', methods = [method])
            def wrapped_func(*args, **kwargs):
                try:
                    if auth:
                        user = None

                        if 'Authorization' in request.httprequest.headers:
                            accessToken = request.httprequest.headers['Authorization']

                            if accessToken and accessToken.startswith('Bearer '):
                                accessToken = accessToken.split('Bearer ')[1]

                                if accessToken:
                                    user = jwtHelper.decode(accessToken)

                        if user:
                            sessionHelper.set('auth.user', user)
                        else:
                            return UnauthorizedResponse()

                    return func(*args, **kwargs)
                except:
                    print(f'Some error occurred when trying to process request: {url}')

                    return ErrorResponse()

            return wrapped_func

        return wrapper

    # moduleRoute

    # createAccessToken
    def createAccessToken(self, userData):
        return jwtHelper.create(userData.update({
            'loginTime': datetime.now().strftime('%s')
        }))

    # createAccessToken

# BaseController
