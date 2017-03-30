#!/usr/bin/env python
# encoding: utf-8

"""
@author: zj
@site  :
@file: views.py
@time: 2017/3/30 下午5:06
@SOFTWARE:PyCharm
"""
from django.http import HttpResponse,JsonResponse
from django.views.generic import View
#点击唱歌主页面
def SingList(request):
    """
    apiurl:/api/v1/singlist/
    请求方法GET
    banner_list:BANNER列表
        bannerid:bannerid
        title：标题
        content：内容
        imgurl:图像地址
        linkurl：链接地址
    recommended_list:推荐列表
        title:标题
        musicname：歌曲名字
        singer：歌手
        authname:发布者
        vediourl
        vediopic
    new_list:
        title:标题
        musicname：歌曲名字
        singer：歌手
        authname:发布者
        vediourl
        vediopic
        
    :param request: 
    :return: 
    """

    data = {
            'banner_list':[{'bannerid':1,'title':'one banner','content':'xxxxx','imgurl':'http://www.dd.com/jj.jpg','linkurl':'http://www.dd.com/jjj.jpg'},
                                              {'bannerid': 1, 'title': 'one banner', 'content': 'xxxxx',
                                               'imgurl': 'http://www.dd.com/jj.jpg',
                                               'linkurl': 'http://www.dd.com/jjj.jpg'},],
            'recommended_list': [{'accompanyid':1,'title': 'this is a song', 'musicname': 'oncemore', 'singer':'zhoujielun',
                          'authname': 'eric', 'vediourl': 'http://www.sxxx.com',
                          'vediopic': 'http://xxx.com/vedio.jpg'}],
            'new_list': [{'accompanyid':2,'title': 'this is a song', 'musicname': 'oncemore', 'singer':'wangd',
                           'authname': 'eric', 'vediourl': 'http://www.sxxx.com',
                           'vediopic': 'http://xxx.com/vedio.jpg'}]
            }

    content = JsonResponse(data)
    return content

#下载伴奏准备唱歌
def StartSing(request,accompanyid):
    """
    apiurl:/api/v1/music/downaccompany?pk={}
    请求方法POST
    请求字段:
    accompanyid:伴奏ID
    accompanyurl: 伴奏文件地址
    lyrics:歌词文件地址
    
    username:我的昵称
    imgtx:我的头像
    auth:
        username：伴奏另一半发起者
        imgtx:伴奏发起者头像
    
    
    :param request: 
    :param musicid: 
    :return: 
    """
    data={'accompanyid':1,'accompanyurl':'http:wdve','lyrics':'http://','user':'eric','imgtx':'http:',
          'auth':[{'username':'dewdwe','imgtx':'http://ewfwe'}]

    }
    content = JsonResponse(data)
    return content

#唱歌完毕要进行的操作
class SingControl(View):

    def post(self,request,*args,**kwargs):
        slug=self.kwargs.get('slug')

        if slug=='keepsing':
            return self.keepsing(request)
        elif slug=='report':
            return self.report(request)
