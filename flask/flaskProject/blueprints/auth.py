import random
import string
from exts import db
from flask import Blueprint,jsonify,render_template,request,redirect,url_for
from exts import mail
from flask_mail import Message
from flask import request
from models import EmailCaptchaModel,UserModel
from .forms import RegisterForm
from werkzeug.security import generate_password_hash,check_password_hash
# /auth
bp= Blueprint('auth', __name__, url_prefix='/auth')
@bp.route('/login')
def login():
    return "这个"

@bp.route('/register' ,methods=['GET','POST'])
def register():
  #pip install  flask-wtf表单验证
    if request.method == "GET":
        return render_template("register.html")
    else:
        form = RegisterForm(request.form)
        if form.validate():
           email = form.email.data
           username = form.username.data
           password = form.password.data
           user=UserModel(email=email,username=username,password=generate_password_hash(password))
           db.session.add(user)
           db.session.commit()
           return  redirect(url_for('auth.login'))
        else:
            return redirect(url_for('auth.register'))


@bp.route('/captcha/email')
def get_email_captcha():
    email = request.args.get('email')
    # 随机数字知母
    sourse=string.digits*4
    captcha=random.sample(sourse,4)
    captcha=''.join(captcha)
    message = Message(subject='注册验证码', recipients=[email], body=f'你的验证码是{captcha}')
    mail.send(message)

    # 用数据库存储
    email_captcha=EmailCaptchaModel(email=email, captcha=captcha)
    db.session.add(email_captcha)
    db.session.commit()
    return jsonify({"code":200,"msg":"","data":None})

@bp.route('/mail/test')
def mail_test():
    message = Message(subject='Test Message', recipients=['1034593934@qq.com'],body='Test Message')
    mail.send(message)
    return 'OK'


