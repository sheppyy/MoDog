import os

# mysql数据库配置
SQLALCHEMY_DATABASE_URI = 'mysql://root:111111@127.0.0.1/modog'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_MODIFICATIONS = True
SQLALCHEMY_ECHO = False
SQLALCHEMY_ENCODING = 'utf-8'
# 启动调试
DEBUG = True
# flask项目运行的端口
SERVERPORT = 9999

# 路径redis数据库配置
REDIS_URL = 'redis://127.0.0.1:6379/0'

# 项目根目录路径
BASE_URL = '/'.join(os.getcwd().split('\\')[:-1])
