# coding:utf-8
from flask import Blueprint, jsonify, request, json
from app.models import User
from app import auth, db, app
import requests

user = Blueprint('user', __name__)

@user.route('/')
def index():
    return "hello world~ 孙博衍~"

@user.route("/login", methods=['POST'])
def login():
    resp = {'msg': 'info', 'data': {}, 'token': ''}

    data = request.json['data']

    wxurl = f'https://api.weixin.qq.com/sns/jscode2session?appid={app.config["MPID"]}&secret={app.config["MPKEY"]}&js_code={data["code"]}&grant_type=authorization_code'
    req = requests.get(wxurl).text
    openid = json.loads(req)['openid']

    userinfo = User.query.filter_by(openid=openid).first()
    if not userinfo:
        r_user = User()
        r_user.name = data['nickName']
        r_user.gender = data['gender']
        r_user.city = data['city']
        r_user.province = data['province']
        r_user.country = data['country']
        r_user.img = data['avatarUrl']
        r_user.openid = openid

        db.session.add(r_user)
        db.session.commit()

        userinfo = r_user

    resp['data'] = userinfo.to_json()
    resp['msg'] = 'login / register success'
    resp['token'] = userinfo.generate_auth_token()

    return jsonify(resp)


@user.route("/check_token")
@auth.login_required
def token():
    return jsonify({'code': 200, 'message': 'check token success'})
