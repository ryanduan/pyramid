#!/usr/bin/env python
# encoding: utf-8

"""
@author: zj
@site  :
@file: views.py
@time: 2017/3/30 下午1:55
@SOFTWARE:PyCharm
"""
from django.http import HttpResponse,JsonResponse


#banner
def Banner(request):
    """
    apiurl:/api/v1/banner/
    请求方法get
    banner_list:
        bannerid:bannerid
        title：标题
        content：内容
        imgurl:图像地址
        linkurl：链接地址
    
    :param request: 
    :return: 
    """
    data = {"status_code": 200,'banner_list':[{'bannerid':1,'title':'one banner','content':'xxxxx','imgurl':'http://www.dd.com/jj.jpg','linkurl':'http://www.dd.com/jjj.jpg'},
                                              {'bannerid': 1, 'title': 'one banner', 'content': 'xxxxx',
                                               'imgurl': 'http://www.dd.com/jj.jpg',
                                               'linkurl': 'http://www.dd.com/jjj.jpg'},]}
    content = JsonResponse(data)
    return content


#搜索菜单
def SearchMusic(request):

    """
                apiurl:/api/v1/search/
                请求方法:GET 
                参数 word:用书请求搜索的关键字

                返回数据：
                
                userid:用户id
                username:用户名称
                description:个人介绍
                fllowerstatus:是否已经关注（1是，0否）
                recording：作品数
                followers：粉丝数
                following：主动关注人数

                obj_list:加载的歌曲数据(列表)
                    musicid:歌曲ID
                    title：歌曲标题
                    musicname:歌曲名称
                    singer：歌手
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
    word = request.GET.get('word', '')
    data = {'userid': 2, 'username': 'eric', 'description': 'this is description!', 'fllowerstatus': 0,
            'recording': 7, 'followers': 2222,
            'following': 15,
            'obj_list': [{'musicid':1,'title': 'this is a song', 'musicname': 'oncemore','singer':'dddd','praise': 260, 'views': 1200,
                           'vediourl': 'http://www.sxxx.com',
                          'vediopic': 'http://xxx.com/vedio.jpg','auth':{'username':'wef','imgtx':'http://'},'participant':{'username':'erferf','imgtx':'http://dew'}}]}

    content = JsonResponse(data)
    return content

#播放视频歌曲
def PlayMusic(request,musicid):
    """
    apiurl:/api/v1/music/play?musicid={{musicid}}/
    请求方法：GET
    请求参数:musicid:视频ID
    
    onj_list:
        musicid:音乐ID
        titleL:音乐标题
        musicname:歌曲名称
        singer：歌手
        praise: 被赞次数
        comment：评论次数
        share:分享次数
        views：观看次数
            auth :作者
                username:用户名
                tximg:头像地址
                            
            participant:参与合唱者
                username:用户名
                tximg:头像地址
        vediourl:视屏文件地址
        vediopic: 视屏截图地址
    comment_list:
        userid:评论人ID
        username：评论人昵称
        comment:评论内容
        
    :param request: 
    :param musicid: 
    :return: 
    """
    data={
        'obj_list': [{'musicid':1,'title': 'this is a song', 'musicname': 'oncemore','singer':'wqe', 'praise': 260,'comment':16,'share':26, 'views': 1200,
                         'vediourl': 'http://www.sxxx.com','vediopic': 'http://xxx.com/vedio.jpg',
                      'auth': {'username': 'wef', 'imgtx': 'http://'},
                      'participant': {'username': 'erferf', 'imgtx': 'http://dew'}}],
        'comment_list':[{'userid':22,'username':'worf','comment':'this is very nice!'},
                        {'userid':32,'username':'worf2','comment':'this is very nice!'}]
    }
    content=JsonResponse(data)
    return content

#视屏点赞
def Praise(request,musicid):
    """
    apiurl:/api/v1/praise?musicid={{musicid}}
    请求方法：post
    请求参数：musicid:视频ID
    
    :param request: 
    :param musicid: 
    :return: 
    """
    data={"status_code":200}
    content=JsonResponse(data)
    return content

#视屏评论
def Comment(request,musicid):
    """
    请求方法：GET
    请求参数:musicid:视频ID
    
    apiurl:/api/v1/comment?musicid={{musicid}}
    
    userid:用户id
    username:用户名称
    parentcomment_id:父级评论ID(可以为空)
    paretcomment_user:父级评论用户名(可以为空)
    comment:评论内容
    create_time:创建时间
    praisestatus:是否被我赞过:{1是0否}
    
    :param request: 
    :param musicid: 
    :return: 
    """
    data={
        'comment_list':[{'userid':22,'username':'worf','parentcomment_id':3,'parentcomment_user':'buzd','comment':'this is very nice!','create_time':4,'praisestatus':0},
                        {'userid':32,'username':'worf2','comment':'this is very nice!','create_time':4,'praisestatus':1}]
    }
    content = JsonResponse(data)
    return content

#发送评论
def PostComment(request,musicid,commentid):
    """
    apiurl:/api/v1/postcomment?musicid={{musicid}}&commentid={{commentid}}
    
    请求方法：post
    请求参数：musicid:被评论的视频ID
            commentid：被回复评论ID
            comment:评论内容
            
    :param request: 
    :param musicid: 
    :return: 
    """
    data = {"status_code": 200}
    content = JsonResponse(data)
    return content


# 评论点赞
def PraisePomment(request, commentid):
    """
    apiurl:/api/v1/praisecomment?commentid={{commentid}}
    请求方法：post
    请求参数：commentid:评论ID

    :param request: 
    :param commentid: 
    :return: 
    """
    data = {"status_code": 200}
    content = JsonResponse(data)
    return content

#分享
def Share(request,musicid):
    """
    apiurl:/api/v1/sharemusic?musicid={{musicid}}
    请求方法:post
    请求参数：misicid:分享视频ID
            content:分享的话
            sharewhere:分享到哪个网站
            
    :param request: 
    :param musicid: 
    :return: 
    """
    musicid=musicid
    content=request.POST.get('content','')
    sharewhere=request.POST.get('sharewhere','')
    data = {"status_code": 200}
    content = JsonResponse(data)
    return content

#收藏
def Collect(request,musicid):
    """
    aipurl:/api/v1/collect?musicid={{musicid}}
    请求方法：POST
    请求参数:musicid:视屏ID
    
    :param request: 
    :param musicid: 
    :return: 
    """
    #用户收藏表对应+1

    data = {"status_code": 200}
    content = JsonResponse(data)
    return content

