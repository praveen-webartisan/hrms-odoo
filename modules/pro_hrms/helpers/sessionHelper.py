# Odoo modules
from odoo import http
from odoo.http import request

'''
IMPORTANT:
    Do only call these methods inside a controller method or it's immediate decorator
'''

# set: Set data in the request session.
def set(key, value):
    context = request.env.context.copy()
    context.update({ key: value })
    request.env.context = context

# set

# get: Get data from the request session.
def get(key):
    return request.context.get(key)

# get
