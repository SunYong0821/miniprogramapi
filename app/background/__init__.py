# coding:utf-8
from flask import Blueprint, Response

bg = Blueprint('background', __name__)

def show(url):
    with open(url, 'rb') as sf:
        content = sf.read()
        return content

@bg.route('/helix')
def helix():
    image = show('./app/background/helix.jpg')
    resp = Response(image, mimetype="image/jpeg")
    return resp
