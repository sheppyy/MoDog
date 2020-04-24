import json
import os
import time
import traceback
import uuid

import redis


import requests
import re

from config.local_settings import BASE_URL


def spider():
    url = 'https://www.pearvideo.com/'
    # 请求网页
    res = requests.get(url)
    # 模仿浏览器头
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/75.0.3770.142 Safari/537.36'
    }
    # 获取网页源文件
    html = res.text
    video_ids = re.findall('<a href="(.*?)" class="vervideo-lilink actplay">', html)
    for item in video_ids:
        try:
            res = requests.get(url + item)
            content = res.text
            title_cover = re.search('<img class="img" src="(.*?)" alt="(.*?)">', content)
            # 获取视频的标题
            cover = title_cover.group(1)
            # 视频封面
            title = title_cover.group(2)
            # 视频日期
            date = re.search('<div class="date">(.*?)</div>', content).group(1)
            # 视频喜欢
            fav = re.search('<div class="fav" data-id=".*?">(.*?)</div>', content).group(1)
            # 视频概述
            summary = re.search('<div class="summary">(.*?)</div>', content).group(1)
            # 视频标签
            tags = re.findall('<span class="tag">(.*?)</span>', content)
            # 以当前时间戳为文件命名
            filename = int(time.time())

            # 获取视频连接
            video_url = re.findall('srcUrl="(.*?).mp4"', content)[0]

            # 下载视频 这不下载视频 网速查
            # result = requests.get(video_url + '.mp4',  header)
            # # 将视频保存到文件
            # with open(BASE_URL + '/static/video/{}.mp4'.format(filename), 'wb') as f:
            #     f.write(result.content)

            new = {
                'id': uuid.uuid4().hex,
                'title': title,
                'cover': cover,
                'date': date,
                'fav': fav,
                'summary': summary,
                'tags': tags,
                'filename': filename,
                'video_url': video_url
            }
            # 保存信息到redis数据库
            rds = redis.Redis(host='localhost', port=6379, db=0)
            rds.lpush('news', json.dumps(new))
            print(title + ' successful!')
        except:
            traceback.print_exc()
            print(url + item)

            # 上面不下载视频 这里也要注释掉
            # if os.path.exists(BASE_URL+'/static/video/'+filename+'.mp4'):
            #     os.remove(BASE_URL+'/static/video/'+filename+'.mp4')
            #     print('delete', BASE_URL+'/static/video/'+filename+'.mp4')

            # 删除redis数据库中异常的数据
            """
            Redis Lrem 根据参数 COUNT 的值，移除列表中与参数 VALUE 相等的元素。
            COUNT 的值可以是以下几种：
            count > 0 : 从表头开始向表尾搜索，移除与 VALUE 相等的元素，数量为 COUNT 。
            count < 0 : 从表尾开始向表头搜索，移除与 VALUE 相等的元素，数量为 COUNT 的绝对值。
            count = 0 : 移除表中所有与 VALUE 相等的值。
            """
            try:
                rds.lrem(name='news', count=-1, value=json.dumps(new))
            except:
                pass
            print('one failed！')
        finally:
            rds.close()


if __name__ == '__main__':
    spider()
