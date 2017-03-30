# -*- coding: utf-8 -*-

"""
Create at 2017/3/30
"""

__author__ = 'TT'

from dao.models.music import Music
from rest_framework import viewsets
from serilizers import MusicListSerializer


class MusicView(viewsets.ViewSet):
    """"""
    serializer_class = MusicListSerializer

    def get_queryset(self):
        return Music.objects.filter(is_enable=1).order_by('-score')

