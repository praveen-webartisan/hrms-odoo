import json

# Odoo modules

# Custom modules
from odoo.addons.pro_hrms.controllers.BaseController import BaseController
from odoo.addons.pro_hrms.helpers import authHelper
from odoo.addons.pro_hrms.helpers import sessionHelper

# AuthController
class AuthController(BaseController):
    # loginUser
    @BaseController.moduleRoute('auth/login', 'POST', False)
    @authHelper.authenticatedUser
    def loginUser(self, **kw):
        validationErrors = {
            'db': 'Required',
            'login': 'Required',
            'password': 'Required',
        }

        if kw:
            if 'db' in kw and kw['db']:
                del validationErrors['db']
            else:
                validationErrors['db'] = 'Required'

            if 'login' in kw and kw['login']:
                del validationErrors['login']
            else:
                validationErrors['login'] = 'Required'

            if 'password' in kw and kw['password']:
                del validationErrors['password']
            else:
                validationErrors['password'] = 'Required'

        if validationErrors:
            return {
                'validationErrors': validationErrors,
            }

        [db, login, password] = kw.values()

        print('AuthController->loginUser()', db, login, password)
        print('hrmsOdooTestVar:', sessionHelper.get('hrmsOdooTestVar'))

        token = authHelper.createAccessToken({
            'db': db,
            'login': login,
        })

        return {
            'token': token
        }

    # loginUser

# AuthController
