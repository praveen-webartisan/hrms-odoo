from odoo import http
from odoo.http import request
import json
from odoo.addons.pro_hrms.helpers import jwtHelper

class AuthController(http.Controller):
    @http.route(['/hrms/api/auth/login'], type = 'json', auth = 'public', methods = ['POST'])
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

        token = jwtHelper.create({
            'db': db,
            'login': login,
        })

        return {
            'token': token
        }
