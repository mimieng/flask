from flask import Flask, render_template, session,g
import config
from exts import db ,mail
from blueprints.qa import bp as qa_bp
from blueprints.auth import bp as auth_bp
from models import UserModel
from flask_migrate import Migrate
app = Flask(__name__)

app.config.from_object(config)

db.init_app(app)
mail.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(qa_bp)

app.register_blueprint(auth_bp)
# flask db init  只需要执行一次
# flask db migrate  将orm模型迁移脚本
# flask db upgrade 将迁移脚本映射到数据库

@app.before_request
def my_before_request():
    user_id = session.get('user_id')
    if user_id :
        user = UserModel.query.get(user_id)
        setattr(g, 'user', user)
    else:
        setattr(g, 'user', None)

@app.context_processor
def my_context_processor():
    return {'user': g.user}

if __name__ == '__main__':
    app.run()
