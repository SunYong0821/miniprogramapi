from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPTokenAuth

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    print(request.headers['X-Forwarded-For'])
    return render_template('index.html')

app.config.from_pyfile('./config.py')

db = SQLAlchemy(app)

auth = HTTPTokenAuth(scheme='Token')

# 所有对象要在注册之前初始化，否则找不到该对象
from app.user import user
from app.background import bg

app.register_blueprint(user, url_prefix="/user/api")
app.register_blueprint(bg, url_prefix="/bg")
