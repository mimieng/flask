from flask import Flask, render_template
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

if __name__ == '__main__':
    app.run()
