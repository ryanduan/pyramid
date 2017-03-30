#!/usr/bin/env python
# encoding: utf-8

"""
@author: zj
@site  :
@file: serializers.py
@time: 2017/3/29 下午3:32
@SOFTWARE:PyCharm
"""
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email','first_name')
