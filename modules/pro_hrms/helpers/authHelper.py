# Odoo modules
from odoo.http import request

# Custom modules
from odoo.addons.pro_hrms.helpers import jwtHelper

# createAccessToken
def createAccessToken(user):
    return jwtHelper.create(user)

# createAccessToken

# authenticatedUser
def authenticatedUser(func):
    def wrapper(*args, **kwargs):
        accessToken = None

        if 'Authorization' in request.httprequest.headers:
            accessToken = request.httprequest.headers['Authorization']

            if accessToken and accessToken.startswith('Bearer '):
                accessToken = accessToken.split('Bearer ')[1]

        print('accessToken:', accessToken)

        return func(*args, **kwargs)

    return wrapper
    # user = None

    # try:
    #     user = jwtHelper.decode(token)
    # except:
    #     user = None

    # return user

# authenticatedUser
