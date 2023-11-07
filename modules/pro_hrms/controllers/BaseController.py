from typing import Final

# Odoo modules
from odoo import http

# Custom modules
from odoo.addons.pro_hrms.helpers import sessionHelper

# BaseController
class BaseController(http.Controller):
    __MODULE_URL_PREFIX: Final = '/hrms/api'

    @staticmethod
    def moduleRoute(url, method, auth):
        # Format module API URL
        if not url.startswith('/'):
            url = BaseController.__MODULE_URL_PREFIX + '/' + url

        def wrapper(func):
            @http.route([url], type = 'json', auth = 'public', methods = [method])
            def wrapped_func(*args, **kwargs):
                sessionHelper.set('hrmsOdooTestVar', 'This is a test context variable.')

                return func(*args, **kwargs)

            return wrapped_func

        return wrapper    

# BaseController
