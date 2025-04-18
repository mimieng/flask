# 数据库配置
HOSTNAME = 'localhost'
PORT     = '3306'
DATABASE = 'zhiliaooa'
USERNAME = 'root'
PASSWORD = '123456'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI


MAIL_SERVER = 'smtp.qq.com'
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = '2900135517@qq.com'
MAIL_PASSWORD = 'vupcrrmcpvehdcjj'
MAIL_DEFAULT_SENDER = '2900135517@qq.com'
