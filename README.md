# MoDog

### 案例说明

MoDog是一个基于flask实现的案例，零零碎碎涉及了爬虫（requests）、redis、jQuery、bootstrap（其实前面这两个我也不知道用了没有...）、Dplayer（弹幕组件）等。



数据的流向大概为：

1. 爬虫从网页收集数据，存到数据库
2. 从数据库获取数据，随机返回5条数据给页面

### 开始

1. 下载

   ```
   git clone https://github.com/sheppyy/MoDog.git
   ```

2. 配置config\local_setttings.py文件

   该文件主要配置MySQL和redis，改成自己的即可，其他的按需改。其实这里用不到MySQL，习惯性的搭一下...。

3. 创建虚拟环境

   为了不要影响自己的环境，很建议建新的环境。

   ```
   pip install -r requirements.txt
   ```

4. 准备数据，本案例的数据来自[梨视频](https://www.pearvideo.com/)

   运行libs\pear_spider.py，从梨视频首页抽信息，信息包括

   * title             标题
   * cover          视频封面
   * date            视频发布的日期
   * fav               视频收藏的人数
   * summary    视频概述
   * tags              视频标签
   * video_url     视频地址

   因为我的网络差，没有对图片视频等下载，只保存了地址...

5. 运行项目

   ```py
   python manage.py runserver
   ```

### 效果

#### 原网站的图：

![res5](https://github.com/sheppyy/MoDog/blob/master/static/img/res4.png)

![res5](https://github.com/sheppyy/MoDog/blob/master/static/img/res5.png)



#### 本案例的图：

![res5](https://github.com/sheppyy/MoDog/blob/master/static/img/res3.png)

![res5](https://github.com/sheppyy/MoDog/blob/master/static/img/res6.png)

# 说明

- 现在不知道为啥，下载离线的[Dplayer](https://github.com/MoePlayer/DPlayer)是没有.css和两个.map，没有.map，好像也问题不大，就报错，还能跑。

- 不用离线的Dplayer，可以到[cdn网站](https://www.bootcdn.cn/)搜索，复制链接到项目即可

- 本案例的Dplayer.min.css是我修改了的

  修改原因：

  ![res5](https://github.com/sheppyy/MoDog/blob/master/static/img/res1.png)

  这里的样式我在外部怎么都强制改不了（太菜了...）。只能对源码下手了...

  修改了的内容：

  ![res5](https://github.com/sheppyy/MoDog/blob/master/static/img/res2.png)

  修改了width: 33%; --->width: auto;

  增加了margin:0px 5px;



到此，结束了。。。蟹蟹
