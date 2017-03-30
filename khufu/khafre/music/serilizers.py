# -*- coding: utf-8 -*-

"""
Create at 2017/3/30
"""

__author__ = 'TT'

from rest_framework import serializers
from khufu.settings import STORAGE_DOMAIN
from dao.models.music import Music


class MusicListSerializer(serializers.ModelSerializer):
    """这里定义一个serializer的类，用来初始化数据库对应的表Music的字段"""
    song_name = serializers.CharField()
    singer_name = serializers.CharField()
    country = serializers.CharField()
    language = serializers.CharField()
    kgame = serializers.SerializerMethodField()
    accompany = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    lyrics = serializers.SerializerMethodField()

    is_hot = serializers.BooleanField()
    is_new = serializers.BooleanField()
    # is_enable = serializers.BooleanField()
    status = serializers.IntegerField()

    def get_accompany(self, obj):
        """这里对应上面的MethodField，通过这个函数处理后返回
        伴奏文件，数据库里存歌词文件的名字，这里拼接成完整的链接地址返回"""
        return '{}/{}'.format(STORAGE_DOMAIN, obj.accompany)

    def get_kgame(self, obj):
        """"""
        return '{}/{}'.format(STORAGE_DOMAIN, obj.kgame)

    def get_image(self, obj):
        """"""
        return '{}/{}'.format(STORAGE_DOMAIN, obj.image)

    def get_lyrics(self, obj):
        """"""
        return '{}/{}'.format(STORAGE_DOMAIN, obj.lyrics)

    class Meta:
        model = Music
        fields = ['id', 'song_name', 'singer_name', 'country', 'language',
                  'kgame', 'accompany', 'image', 'lyrics', 'is_hot', 'is_new', 'status']