#!/usr/bin/env python
# encoding: utf-8

"""
@author: zj
@site  :
@file: views.py
@time: 2017/3/29 下午3:33
@SOFTWARE:PyCharm
"""
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from khafre.account.serializers import AccountSerializer

from django.http import HttpResponse, JsonResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.generic import View
from django.contrib import auth

@csrf_exempt
def user_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        users = User.objects.all()
        serializer = AccountSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AccountSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class UserControl(View):
    #获取用户需要进行什么操作

    def get(self,request,*args,**kwargs):

        if not request.user.is_authenticated():
            return HttpResponse('LOGIN FIRST!')

        slug=self.kwargs.get('slug')
        pk=self.kwargs.get('pk')
        if slug=='userlist':
            return self.userlist(request,userid=pk)
        elif slug=='me':
            return self.myself(request)
        elif slug=='recording':
            return self.recording(request,userid=pk)
        elif slug=='fllowers':
            return self.fllowers(request,userid=pk)
        elif slug=='fllowing':
            return self.fllowers(request,userid=pk)


        return super(UserControl,self).get(request,*args,**kwargs)


    def post(self,request,*args,**kwargs):
        slug=self.kwargs.get('slug')
        pk=self.kwargs.get('pk')
        if slug=='block':
            return self.block(request,userid=pk)
        elif slug=='fllow':
            return self.fllow(request,userid=pk)

    #查看用户数据
    def userlist(self,request,userid):

        """
            apiurl:/api/v1/usercontrol/userlist{userid}/
            请求方法:GET 
            参数 userid

            返回数据：
            点击用户头像（用户是自己还是别人）进入查看用户信息
            userid:用户id
            username:用户名称
            description:个人介绍
            tximg:头像地址
            fllowerstatus:是否已经关注（1是，0否）
            recording：作品数
            followers：粉丝数
            following：主动关注人数

            obj_list:加载的歌曲数据(列表)
                title：歌曲标题
                musicname:歌曲名称
                singer:歌手
                praise:被赞次数
                views:被观看次数
                auth :作者
                            username:用户名
                            tximg:头像地址
                            
                participant:参与合唱者
                            username:用户名
                            tximg:头像地址
                vediourl：视频地址
                vediopic:展示图片地址

            :param request: 
            :return: 
            """
        data = {'userid': 2, 'username': 'eric', 'description': 'this is description!','tximg':'http://baidu.com/sss.jpg', 'fllowerstatus': 0,
                'recording': 7, 'followers': 2222,
                'following': 15,
                'obj_list': [{'title': 'this is a song', 'musicname': 'oncemore', 'singer':'3edfe','praise': 260, 'views': 1200,
                               'vediourl': 'http://www.sxxx.com','vediopic': 'http://xxx.com/vedio.jpg',
                              'auth': {'username': 'wef', 'imgtx': 'http://'},
                              'participant': {'username': 'erferf', 'imgtx': 'http://dew'}}]}

        content = JsonResponse(data)
        return content

    #查看自己
    def myself(self,request):
        """
        apiurl:/api/v1/usercontrol/me
        请求方法：get
        
        返回数据
        userid:用户id
        username：用户名
        description:个人介绍
        tximg:头像地址
        recording：作品数
        followers：粉丝数
        following：主动关注人数
        
        obj_list:加载的歌曲数据(列表)
                title：歌曲标题
                musicname:歌曲名称
                praise:被赞次数
                views:被观看次数
                authname:作者
                participant:参与合唱者
                vediourl：视频地址
                vediopic:展示图片地址
        save_list:加载的歌曲数据(列表)
                title：歌曲标题
                musicname:歌曲名称
                praise:被赞次数
                views:被观看次数
                auth :作者
                            username:用户名
                            tximg:头像地址
                            
                participant:参与合唱者
                            username:用户名
                            tximg:头像地址
                vediourl：视频地址
                vediopic:展示图片地址
        :param request: 
        :return: 
        """
        data = {'userid': 2, 'username': 'eric', 'description': 'this is description!','tximg':'http://www.dd.com/sss.jpg', 'fllowerstatus': 0,
                'recording': 7, 'followers': 2222,
                'following': 15,
                'obj_list': [{'title': 'this is a song', 'musicname': 'oncemore', 'praise': 260, 'views': 1200,'vediourl': 'http://www.sxxx.com',
                              'vediopic': 'http://xxx.com/vedio.jpg',
                              'auth': {'username': 'wef', 'imgtx': 'http://'},
                              'participant': {'username': 'erferf', 'imgtx': 'http://dew'}
                              }],
                'save_list':[{'title': 'this is a song', 'musicname': 'oncemore', 'praise': 260, 'views': 1200,
                             'vediourl': 'http://www.sxxx.com','vediopic': 'http://xxx.com/vedio.jpg',
                              'auth': {'username': 'wef', 'imgtx': 'http://'},
                              'participant': {'username': 'erferf', 'imgtx': 'http://dew'}
                              }]
                }


        content = JsonResponse(data)
        return content
    #查看用户作品
    def recording(self,request,userid):
        """
            apiurl:/api/v1/usercontrol/recording{userid}/
            请求方法:GET 
            参数 userid

            返回数据：
            点击用户头像（非自己）进入查看用户信息
            userid:用户id
            username:用户名称
            

            obj_list:加载的歌曲数据(列表)
                title：歌曲标题
                musicname:歌曲名称
                praise:被赞次数
                views:被观看次数
                auth :作者
                            username:用户名
                            tximg:头像地址
                            
                participant:参与合唱者
                            username:用户名
                            tximg:头像地址
                vediourl：视频地址
                vediopic:展示图片地址

            :param request: 
            :param userid: 
            :return: 
            """
        data = {'userid': 2, 'username': 'eric',
                'obj_list': [{'title': 'this is a song', 'musicname': 'oncemore', 'praise': 260, 'views': 1200,
                              'vediourl': 'http://www.sxxx.com', 'vediopic': 'http://xxx.com/vedio.jpg',
                              'auth': {'username': 'wef', 'imgtx': 'http://'},
                              'participant': {'username': 'erferf', 'imgtx': 'http://dew'}
                              }]}
        content = JsonResponse(data)
        return content

    #查看用户粉丝
    def fllowers(self,request,userid):
        """
            apiurl:/api/v1/usercontrol/fllowers{userid}/
            请求方法:GET 
            参数 userid

            返回数据：

            userid:用户id
            username:用户名称
            description:个人介绍
            fllowerstatus:是否已经关注（1是，0否）
            recording：作品数
            followers：粉丝数
            following：主动关注人数
            :param request: 
            :param userid: 
            :return: 
            """
        data = {'userid': 2, 'username': 'eric', 'description': 'this is description!', 'fllowrrstatus': 0}

        content = JsonResponse(data)
        return content

    #拉黑用户
    def block(self,request,userid):
        """
        apiurl: /api/v1/usercontrol/block{userid}/
        请求方法:POST
        参数
        userid
        
        :param request: 
        :param userid: 
        :return: 
        """

        return HttpResponseRedirect('/api/v1/hotmusic/')

    #关注用户
    def fllow(self,request,userid):
        """
        apiurl:/api/v1/usercontrol/fllow{userid}
        :param request: 
        :param userid: 
        :return: 
        """
        return HttpResponse('ok')


class settings(View):
    #获取用户需要进行什么操作

    def get(self,request,*args,**kwargs):

        if not request.user.is_authenticated():
            return HttpResponse('LOGIN FIRST!')

        slug=self.kwargs.get('slug')

        if slug=='changepwd':
            return self.changepwd(request)
        elif slug=='profile':
            return self.profile(request)
        elif slug=='socal':
            return self.socal(request)
        elif slug=='help':
            return self.help(request)
        elif slug=='about':
            return self.about(request)
        elif slug=='logout':
            return self.logout(request)
        elif slug=='bolck':
            return self.bolck(request)
        elif slug=='changetx':
            return self.changetx(request)
        return super(settings,self).get(request,*args,**kwargs)

    #更换头像
    def changetx(self,request):
        """
        apiurl:/api/v1/settings/changetx/
        请求方法：POST
        img:头像文件
        :param request: 
        :return: 
        """
        error = "some error"

        data = {"status_code": 200, 'error': error}
        content = JsonResponse(data)
        return content
    #个人资料
    def profile(self,request):
        """
        apiurl:/api/v1/settings/editprofile/
        
        请求方法：POST
        请求参数：userid：用户ID
                username:用户名
                adress:地址
                first_name:
                last_name:
                sex:性别
                description：自我介绍
        :param request: 
        :return: 
        """
        error="some error"

        data = {"status_code": 200,'error':error}
        content = JsonResponse(data)
        return content
    #修改密码
    def changepwd(self,request):
        """
        apiurl:/api/v1/settings/changepwd/
        currentpwd:旧密码
        newpwd1:新密码1
        newpwd2:新密码2
        :param request: 
        :return: 
        """

        error="error!"

        data={"status_code": 200,'error':error}
        content = JsonResponse(data)
        return content

    #黑名单目录
    def bolck(self,request):
        """
        APIURL：/api/v1/settings/bolck/
        请求方法GET
        userid：用户id
        username：用户名
        description:用户介绍
        
        :param request: 
        :return: 
        """
        data = {"status_code": 200,
                'bolck_list':[{'userid':1,'username':'efwfewf','description':'just about me'}]}
        content = JsonResponse(data)
        return content

    #拉白
    def delbolck(self,request):
        """
        apiurl:/api/v1/delbolck?userid={{userid}}
        userid:用户id
        请求方法:post
        参数：userid:用户id
        
        :param request: 
        :return: 
        """
        error = "error!"

        data = {"status_code": 200,'error': error}
        content = JsonResponse(data)
        return content
    #社交绑定
    def socal(self,request):
        """
        apiurl:/auth/login/facebook/?next=/
        :param request: 
        :return: 
        """
        pass

    #帮助和建议
    def help(self,request):
        """
        apiurl:/api/v1/suggest/
        请求方法：POST
        content:内容
        :param request: 
        :return: 
        """
        data = {"status_code": 200}
        content = JsonResponse(data)
        return content

    #关于
    def about(self,request):
        """
        apiurl:/api/v1/aboutus/
        
        title:标题
        content: 内容
        :param request: 
        :return: 
        """
        data={'title':'intune','content':'what XXXXX'}
        content = JsonResponse(data)
        return content

    #登出
    def logout(self,request):
        """
        apiurl:/api/v1/settings/logout/
        请求
        
        :param request: 
        :return: 
        """
        if not request.user.is_authenticated():
            return HttpResponse("not login")
        else:
            auth.logout(request)
            return HttpResponse('ok')

