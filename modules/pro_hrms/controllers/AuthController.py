import json

# Odoo modules
from odoo import http
from odoo.tools import authenticate

# Custom modules
from odoo.addons.pro_hrms.controllers.BaseController import BaseController
from odoo.addons.pro_hrms.helpers import sessionHelper
from odoo.addons.pro_hrms.helpers.moduleResponse import NotFoundResponse, InvalidDataResponse

# AuthController
class AuthController(BaseController):
    # loginUser
    @BaseController.moduleRoute('auth/login', 'POST', False)
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

        if not http.db_filter([db]):
            return NotFoundResponse(f'Database {db} not found in the Odoo instance.')

        try:
            userId = authenticate(db, login, password)

            print('authenticated userId:', userId)
        except odoo.exceptions.AccessDenied:
            return InvalidDataResponse(message = 'Invalid Username/Password. Please check.')

        token = self.createAccessToken({
            'db': db,
            'login': login,
        })

        return {
            'token': token
        }

    # loginUser

# AuthController
