import wtforms
from wtforms.validators import Email, Length,EqualTo,InputRequired
from models import UserModel ,EmailCaptchaModel
from exts import db
# 验证前端表单提交的数据是否符合要求
class RegisterForm(wtforms.Form):
    email = wtforms.StringField(validators=[Email(message="邮箱格式错误")])
    captcha=wtforms.StringField(validators=[Length(min=4, max=4,message='验证吗格式错误')])
    username=wtforms.StringField(validators=[Length(min=3,max=20,message="用户名格式错误")])
    password=wtforms.StringField(validators=[Length(min=6,max=20,message="密码格式错误")])
    password_confirm=wtforms.StringField(validators=[EqualTo("password",message="两次密码不一致")])
    # 之定义验证
    # 邮箱是否被注册过

    def validate_email(self,field):
        email=field.data
        user=UserModel.query.filter_by(email=email).first()
        if user:
            raise wtforms.ValidationError(message="该邮箱已被注册")
 # 验证码是否正确
    def validate_captcha(self, field):
        captcha=field.data
        email=self.email.data
        captcha_models=EmailCaptchaModel.query.filter_by(email=email,captcha=captcha).first()
        if not captcha_models:
            raise wtforms.ValidationError(message="邮箱或验证码错误")
        else:
            db.session.delete(captcha_models)
            db.session.commit()
class LoginForm(wtforms.Form):
    email = wtforms.StringField(validators=[Email(message="邮箱格式错误")])
    password = wtforms.StringField(validators=[Length(min=6, max=20, message="密码格式错误")])

class QuestionForm(wtforms.Form):
    title=wtforms.StringField(validators=[Length(min=3,max=100,message="标题格式错误")])
    content=wtforms.StringField(validators=[Length(min=3,message="内容格式错误")])


class AnswerForm(wtforms.Form):
    content = wtforms.StringField(validators=[Length(min=3, message="内容格式错误")])
    question_id = wtforms.IntegerField(validators=[InputRequired(message="必须要传入问题id！")])
