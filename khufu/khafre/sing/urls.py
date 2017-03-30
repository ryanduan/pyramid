#!/usr/bin/env python
# encoding: utf-8

"""
@author: zj
@site  :
@file: urls.py
@time: 2017/3/30 下午5:06
@SOFTWARE:PyCharm
"""
from django.conf.urls import url, include
from khafre.sing.views import SingList,SingControl

urlpatterns = [

    url(r'^api/v1/singlist/$',SingList,name='singlist'),
    url(r'^api/v1/singcontrol/(?P<slug>\w+)$',SingControl.as_view(),name='singcontrol-view'),


]
