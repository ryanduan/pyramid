#!/usr/bin/env python
# encoding: utf-8

"""
@author: zj
@site  :
@file: urls.py
@time: 2017/3/29 下午12:35
@SOFTWARE:PyCharm
"""
from django.conf.urls import include,url
from khafre.main.main import HotMusic
from khafre.main.views import SearchMusic,Praise,PlayMusic,Comment,PostComment,PraisePomment,Share,Collect,Banner
urlpatterns=[
    url(r'^api/v1/hotmusic/$',HotMusic,name='hotmusic'),
    url(r'^api/v1/search/',SearchMusic,name='search'),
    url(r'^api/v1/praise\d+/$',Praise,name='praise'),
    url(r'^api/v1/music/play\d+/$',PlayMusic,name='play'),
    url(r'^api/v1/comment\d+/$',Comment,name='comment'),
    url(r'^api/v1/postcomment\d+/$',PostComment,name='postcomment'),
    url(r'^api/v1/praisecomment\d+/$',PraisePomment,name='praisecomment'),
    url(r'^api/v1/sharemusic\d+/$',Share,name='sharemusic'),
    url(r'^api/v1/collect\d+/$',Collect,name='collect'),
    url(r'^api/v1/banner/$',Banner,name='banner'),

]