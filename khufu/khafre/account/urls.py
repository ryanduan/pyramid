#!/usr/bin/env python
# encoding: utf-8

"""
@author: zj
@site  :
@file: urls.py
@time: 2017/3/29 下午3:34
@SOFTWARE:PyCharm
"""

from django.conf.urls import url, include
from rest_framework import routers
from khafre.account import views



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^users/$', views.user_list),
    url(r'^auth/',include('rest_framework_social_oauth2.urls')),
    url(r'^api/v1/usercontrol/(?P<slug>\w+)$',views.UserControl.as_view(),name='usercontrol-view'),
    url(r'^api/v1/settings/(?P<slug>\w+)$',views.settings.as_view(),name='settings-view'),
    #url(r'^api/v1/user/userlist\d+/$',views.Users,name='user'),
    #url(r'^api/v1/user/block/\d+/$',views.Users,name='user'),
    #url(r'^api/v1/user/recording/\d+/$',views.UserRecording,name='user'),
]