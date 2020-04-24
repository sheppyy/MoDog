from flask import Flask, render_template

# 创建应用类 继承Flask
from flask_migrate import Migrate
from flask_redis import FlaskRedis
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy


class Application(Flask):
    # 初始化方法
    def __init__(self, import_name):
        # 调用父类(Flask)的初始化方法
        super(Application, self).__init__(import_name)
        # 根据系统环境变量var，从py文件加载配置信息
        self.config.from_pyfile('config/local_settings.py')
        # 重新初始化项目配置信息 等同于 db = SQLAlchemy(app)
        db.init_app(self)


# 实例化db对象
db = SQLAlchemy()
# 实例化app对象
app = Application(__name__)
redis_obj = FlaskRedis(app)


# 404处理
@app.errorhandler(404)
def page_not_found(error):
    return render_template('home/404.html'), 404


# 包装/扩展app对象
manage = Manager(app)

# 1.要使用flask_migrate,必须绑定app和DB
migrate = Migrate(app, db)
