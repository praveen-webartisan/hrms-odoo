from odoo.addons.pro_hrms.helpers import jwtHelper

# createAccessToken
def createAccessToken(user):
    return jwtHelper.create(user)

# createAccessToken

# authenticateUser
def authenticateUser(token):
    user = None

    try:
        user = jwtHelper.decode(token)
    except:
        user = None

    return user

# authenticateUser
