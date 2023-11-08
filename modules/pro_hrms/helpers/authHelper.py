# Odoo modules
from odoo.http import request

# Custom modules
from odoo.addons.pro_hrms.helpers import jwtHelper

# createAccessToken
def createAccessToken(user):
    return jwtHelper.create(user)

# createAccessToken
