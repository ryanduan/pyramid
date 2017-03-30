# -*- coding: utf-8 -*-

"""
Create at 2017/3/21
这里做一个base model 其他model都集成base model
"""

__author__ = 'TT'

from django.db.models import Model, DateTimeField, BooleanField


class Base(Model):
    """"""
    created_at = DateTimeField(null=True, blank=True, auto_now_add=True)
    deleted_at = DateTimeField(null=True, blank=True)

    # is_enable = BooleanField(default=True)
    is_delete = BooleanField(default=False)
