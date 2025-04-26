import random
import string
from exts import db
from flask import Blueprint, jsonify, render_template, request, redirect, url_for, session
from exts import mail
from flask_mail import Message
from flask import request
from models import EmailCaptchaModel,UserModel
from .forms import RegisterForm,LoginForm
from werkzeug.security import generate_password_hash,check_password_hash
# /auth
bp= Blueprint('auth', __name__, url_prefix='/auth')
@bp.route('/login',methods=['GET','POST'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        form=LoginForm(request.form)
        if form.validate():
            email=form.email.data
            password=form.password.data
            user=UserModel.query.filter_by(email=email).first()
            if not user:
                print('用户不存在')
                return redirect(url_for('auth.login'))
            if check_password_hash(user.password,password):

                # cookie不适合存放太多数据
                # cookie一般存储登录授权的东西
                # flask中的session,是经过加密后存储的
                session['user_id']=user.id
                return redirect('/')
            else:
                print('用户不存在')
                return redirect(url_for('auth.login'))
        else:
            print(form.errors)
            return redirect(url_for('auth.login'))

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
            print(form.errors)
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

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))

@bp.route('/mail/test')
def mail_test():
    message = Message(subject='Test Message', recipients=['1034593934@qq.com'],body='Test Message')
    mail.send(message)
    return 'OK'


