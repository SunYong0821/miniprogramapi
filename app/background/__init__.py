# coding:utf-8
from flask import Blueprint

bg = Blueprint('background', __name__)

@bg.route('/helix')
def helix():
    resp = Response(image, mimetype="image/jpeg")
    return resp
