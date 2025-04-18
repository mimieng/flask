import random
import string

from flask import Blueprint
from exts import mail
from flask_mail import Message
from flask import request
# /auth
bp= Blueprint('auth', __name__, url_prefix='/auth')
@bp.route('/login')
def login():
    pass

@bp.route('/register')
def register():
  pass

@bp.route('/captcha/email')
def get_email_captcha():
    email = request.args.get('email')
    # 随机数字知母
    sourse=string.digits*4
    captcha=random.sample(sourse,4)
    captcha=''.join(captcha)
    message = Message(subject='注册验证码', recipients=[email], body=f'你的验证码是{captcha}')
    mail.send(message)
    return "success"

@bp.route('/mail/test')
def mail_test():
    message = Message(subject='Test Message', recipients=['1034593934@qq.com'],body='Test Message')
    mail.send(message)
    return 'OK'


