#!/usr/bin/env python
# encoding: utf-8

"""
@author: zj
@site  :
@file: main.py
@time: 2017/3/29 下午12:38
@SOFTWARE:PyCharm
"""

from django.http import HttpResponse,JsonResponse
import json
from rest_framework.renderers import JSONRenderer
from khafre.account.serializers import AccountSerializer


def HotMusic(request):
    """
    apiURL:/api/v1/hotmusic/
    请求方法：GET 无参数
    热门页面返回数据
    userid:用户id
    username:用户名称
    list:加载的歌曲数据(列表)
        title：歌曲标题
        musicname:歌曲名称
        singer：歌手
        praise:被赞次数
        views:被观看次数
        authname:作者
        participant:参与合唱者
        vediourl：视频地址
        vediopic:展示图片地址
        
    :param request: 
    :return: 
    """

    data={'userid':1,'username':'admin','obj_list':[{'title':'this is a song','musicname':'oncemore','singer':'fewfwef','praise':260,'views':1200,
                                                'authname':'eric','participant':'urdan','vediourl':'http://www.sxxx.com',
                                                     'vediopic':'http://xxx.com/vedio.jpg'}]}

    content=JsonResponse(data)
    #return HttpResponse(json.dumps(data), content_type='application/json')
    return content

