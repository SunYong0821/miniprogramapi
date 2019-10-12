# coding:utf-8
from flask import Blueprint

bg = Blueprint('background', __name__)

def show(url):
    with open(url, 'rb') as 

@bg.route('/helix')
def helix():
    resp = Response(image, mimetype="image/jpeg")
    return resp
