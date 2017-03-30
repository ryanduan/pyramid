# -*- coding: utf-8 -*-

"""
Create at 2017/3/21
歌曲数据模型
"""

__author__ = 'TT'

from base import Base
from django.db.models import CharField, BooleanField, PositiveSmallIntegerField, \
    IntegerField


class Music(Base):
    """音乐表 - 记录 歌曲名，歌手名，国家，语言，分类，推送区域
    伴凑文件，打分文件，封面文件"""
    song_name = CharField(u'歌曲名', max_length=200, db_index=True)
    singer_name = CharField(u'歌手名', max_length=200, db_index=True)
    country = CharField(u'国家', max_length=200)
    language = CharField(u'语言', max_length=100)
    style = CharField(u'分类', max_length=100)
    area = CharField(u'推广区域', max_length=200)
    kgame = CharField(u'打分文件', max_length=100)
    accompany = CharField(u'伴奏文件', max_length=100)
    image = CharField(u'图片', max_length=100)
    lyrics = CharField(u'歌词', max_length=100)

    # 歌曲状态
    is_hot = BooleanField(u'是否最热', default=True)
    is_new = BooleanField(u'是否最新', default=True)
    is_enable = BooleanField(u'是否上架', default=True)
    status = PositiveSmallIntegerField(u'状态', default=1)
    score = IntegerField(u'分数-排序用', default=0)
