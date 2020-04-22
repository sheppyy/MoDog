#基于什么基础的镜像
FROM python:3.6

#代码添加到code文件夹
ADD ./test /code

# 设置code文件夹为工作目录
WORKDIR /code

# 安装支持
RUN pip install -i https://pypi.douban.com/simple/ -r requirements.txt
# RUN pip install flask -i https://pypi.douban.com/simple/

# 执行命令
CMD ["python3", "manage.py", "runserver"]