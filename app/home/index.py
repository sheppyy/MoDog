import datetime
import random
import uuid
from flask import Blueprint, render_template, request, Response, jsonify, redirect, url_for
import json
from application import redis_obj
home = Blueprint('index', __name__)


@home.route('/')
def index():
    data = {
        'data': [],
        'meta': {
            'status': 200,
            'msg': 'success'
        }
    }
    try:
        res = redis_obj.lrange('news', 0, -1)
    except:
        data['meta']['status'] = 500
        data['meta']['msg'] = 'fail'
        return Response(data, mimetype="application/json")

    data['data'] = [json.loads(r) for r in res]
    # 随机返回5个
    return render_template('home/index.html', data=random.sample(data['data'], 5))


@home.route('/to/play', methods=['POST'])
def play():
    # 获取前端传递的数据，再传递到另一个页面
    item = {
        'id': request.values.get('id'),
        'title': request.values.get('title'),
        'cover': request.values.get('cover'),
        'date': request.values.get('date'),
        'fav': request.values.get('fav'),
        'summary': request.values.get('summary'),
        'tags': request.values.get('tags'),
        'filename': request.values.get('filename'),
        'video_url': request.values.get('video_url')
    }
    # 重定向到def show_play():
    return redirect(url_for('index.show_play'))


@home.route('/show', methods=['GET', 'POST'])
def show_play():
    return render_template('home/play.html')


# 地址必须是这样
@home.route('/dm/v3/', methods=['GET', 'POST'])
def dm():
    # 拉取弹幕GET方法
    if request.method == "GET":
        mid = request.args.get("id")
        key = "movie" + str(mid)
        # 取长度
        if redis_obj.llen(key):
            msgs = redis_obj.lrange(key, 0, -1)
            res = {
                "code": 0,
                "data": [json.loads(v) for v in msgs]
            }
        else:
            res = {
                "code": 1,
                "danmaku": []
            }
        response = json.dumps(res)
    # 添加弹幕 POST方法
    if request.method == "POST":
        data = json.loads(request.get_data())
        msg = {
            "__v": 0,
            "_id": datetime.datetime.now().strftime("%Y%m%d%H%M%S") + uuid.uuid4().hex,
            "author": data["author"],
            "time": data["time"],
            "text": data["text"],
            "color": data["color"],
            "type": data["type"],
            "ip": request.remote_addr,
            "player": data["id"]
        }
        res = {
            "code": 0,
            "danmaku": msg
        }

        msg = [data["time"], data["type"], data["color"], data["author"], data["text"]]
        try:
            # 在对应电影的弹幕列表的前面添加应该弹幕
            redis_obj.lpush("movie" + str(data["id"]), json.dumps(msg))
        except:
            res['code'] = 1
            res['danmaku'] = 'fail'
        finally:
            redis_obj.close()

        response = json.dumps(res)

    # redis_obj.close()

    return Response(response, mimetype="application/json")


@home.route('/data', methods=['GET'])
def get_datas():
    data = {
        'data': [],
        'meta': {
            'status': 200,
            'msg': 'success'
        }
    }
    try:
        res = redis_obj.lrange('news', 0, -1)
    except:
        data['meta']['status'] = 500
        data['meta']['msg'] = 'fail'
        return Response(data, mimetype="application/json")

    data['data'] = [json.loads(r) for r in res]
    return jsonify(data)
