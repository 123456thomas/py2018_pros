from django.shortcuts import render,redirect,HttpResponse



from django.template import loader
# JsonResponse用于字典json形式的响应
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
# 用于序列化Django对象的接口
from django.core.serializers import serialize,deserialize

# 导入事务模块
from django.db import transaction
from . import models
# 导入加密模块
import hashlib

# 引入缓存
from django.core.cache import cache

# from . import forms

# 验证码导入模块
from io import BytesIO
from . import utils
# Create your views here.

# 导入分页插件
from django.core.paginator import Paginator
from django.conf import settings

def index(req):
    return render(req, 'index.html')


# 精彩推荐

# 我的圈子
def myblog(req):
    Artf = cache.get('artf')
    if Artf == None:
        Artf = []
        if len(req.session['friend'])>0:
            for u in req.session['friend']:
                obju = models.Users.usermanage.get(username=u.partner)
                temp = models.Articles.objects.filter(fid=obju)
                Artf.extend(temp)
            temps = models.Articles.objects.filter(fid=req.session['user'])
            Artf.extend(temps)
            Artf.sort(key=lambda x:x.ctime,reverse=True)
        cache.set('artf',Artf)
        Artf = cache.get('artf')

    # 获取当前页码
    pagenum = req.GET.get('pagenum', default=1)
    # 构建Paginator对象
    paginator = Paginator(Artf, settings.PAGESIZE)
    # 获取分页对象的列表，参数为当前页码
    page = paginator.page(int(pagenum))
    return render(req, 'usercol/index.html',{'page':page})
# 登陆界面
def login(request):
    # 显示所有用户两天内博客，并按时间推新，每页7条
    # 超链接访问
    if request.method == 'GET':
        return render(request, 'index.html')
    # 注册跳转而来
    elif request.method == 'POST':
        yanzh = request.session['check_code']
        if yanzh != request.POST["code"]:
            return render(request, 'index.html', {'msg': '验证码错误'})
        username = request.POST['username']
        users = models.Users.usermanage.filter(username=username)
        if users.exists():
            user = users.first()
            pwd = request.POST['pwd']
            md = hashlib.md5()
            md.update(pwd.encode('utf8'))
            pwds = md.hexdigest()
            if user.pwd == pwds:
                Arts = models.Articles.objects.filter(fid=user).order_by('-id')
                friendinfo = models.Friends.objects.filter(oid=user, partner="")
                friend = models.Friends.objects.filter(oid=user, offer="")
                # 会话的使用
                request.session['user'] = user
                request.session['friendinfo'] = friendinfo
                request.session['friend'] = friend
                # 缓存的使用
                cache.set('arts', Arts)
                arts = cache.get('arts')
                return redirect('usercol:myblog')
            else:
                msg = '密码错误'
        else:
            msg = '用户名不存在'
        return render(request, 'index.html', {'msg': msg})
def whisper(req):
    # 查询并按id逆序排序
    Arts2 = cache.get('art')
    if Arts2 == None:
        Arts = models.Articles.objects.filter(fid=req.session['user']).order_by('-id')
        cache.set('art', Arts)
        Arts2 = cache.get('art')
    # print(Arts2)
    # 获取当前页码
    pagenum = req.GET.get('pagenum',default=1)
    # 构建Paginator对象
    paginator = Paginator(Arts2,settings.PAGESIZE)
    # 获取分页对象的列表，参数为当前页码
    page = paginator.page(int(pagenum))
    return render(req, 'usercol/whisper.html',{'page':page})



def leacots(req):
    return render(req, 'usercol/leacots.html')

def friendmanage(request):
    friend = models.Friends.objects.get(id=request.GET['friend'])
    friend.delete()
    request.session['friend'] = models.Friends.objects.filter(oid=req.session['user'],offer="")
    return redirect('usercol:my')


# 清除消息
def delinfo(req):
    for u in req.session['friend']:
        if u.partner == "":
            u.delete()
    req.session['friendinfo'] = models.Friends.objects.filter(oid=req.session['user'] ,partner="")
    return redirect('usercol:my')

def album(req):
    return render(req, 'usercol/album.html')
def about(req):
    return render(req, 'usercol/about.html')
def my(req):
    # print(req.session['user2'])
    # 接受消息
    if req.method=='POST':
        friends = models.Friends.objects.get(id=req.POST['offer'])
        friends.partner = friends.offer
        user2 = models.Users.usermanage.get(username=friends.partner)
        friends.offer = ""
        friends.save()
        friends2 = models.Friends(partner=req.session['user'].username, offer="",  oid=user2)
        friends2.save()
        req.session['friendinfo'] = models.Friends.objects.filter(oid=req.session['user'], partner="")
        req.session['friend'] = models.Friends.objects.filter(oid=req.session['user'],offer="")
    return render(req, 'usercol/aboutme.html')

def details(req):
    return render(req, 'usercol/details.html')

# 注册界面
def register(request):
    # 超链接访问
    if request.method == 'GET':
        return render(request, 'register.html')
    # 注册请求
    elif request.method == 'POST':
        username = request.POST['username']
        pwd = request.POST['pwd']
        email = request.POST['email']
        age = request.POST['age']
        user = models.Users.usermanage
        if user.filter(username=username).exists():
            return render(request, 'register.html',{'msg':"该用户名已存在，请重新注册"})
        if len(age)==0:
            age=18
        else:
            age=int(age)
        # 添加新用户
        md = hashlib.md5()
        md.update(pwd.encode('utf8'))
        pwds = md.hexdigest()
        user.Create_user(username, pwds, email, age)
        return render(request, 'index.html',{'msg':'注册成功'})


# 修改个人信息
def update(req):
    print(req.POST)
    username = req.POST['username']
    pwd = req.POST['pwd']
    email = req.POST['email']
    age = req.POST['age']
    user = req.session['user']
    try:
        photo = req.FILES['photo']
    except:
        photo = user.photo
    if pwd != "":
        md = hashlib.md5()
        md.update(pwd.encode('utf8'))
        pwds = md.hexdigest()
        user.pwd = pwds
    user.username = username
    user.email = email
    user.age = int(age)
    user.photo = photo
    user.save()
    # ul = photo.split("/")
    print(user.photo)
    print(photo)
    req.session['user'] = user
    return redirect('usercol:my')


# 查看文章
def article(req,sid):
    arts = models.Articles.objects.filter(id = sid).first()

    return render(req,'usercol/article.html')


# 发表文章
def writing(req):
    if req.method == 'GET':

        return render(req, 'usercol/writing.html')
    elif req.method == 'POST':
        title = req.POST['title']
        content = req.POST['content']
        arts = models.Articles(title = title,content = content,fid = req.session['user'])
        arts.save()

        Arts = models.Articles.objects.filter(fid=req.session['user']).order_by('-id')
        cache.set('arts', Arts)
        return redirect('usercol:whisper')


# 添加好友
def addone(request):
    if request.method=='GET':
        return render(request,'usercol/addone.html')
    elif request.method=='POST':
        user_f = models.Users.usermanage.filter(username=request.POST['name'])

        if user_f.exists():

            user_f = user_f.first()
            print(user_f)
            friend = models.Friends(partner="", offer = request.session['user'].username , oid = user_f)
            friend.save()
            return render(request, 'usercol/index.html')
        else:
            return render(request,'usercol/addone.html',{'msd':'该用户不存在'})

def yanzheng(req):
    # 在内存中开辟空间用以生成临时的图片
    f = BytesIO()
    img, code = utils.create_code()
    # 保存验证码信息到 session 中，方便下次表单提交时进行验证操作
    req.session['check_code'] = code
    img.save(f, 'PNG')
    return HttpResponse(f.getvalue())


# 文章的更新
def artupdate(req):
    arts = models.Articles.objects.get(id=req.POST['aid'])
    if req.POST['update'] == 'update':

        arts.title = req.POST['title']
        arts.content = req.POST['content']
        arts.save()
    elif req.POST['update'] == 'del':
        arts.delete()
    Arts = models.Articles.objects.filter(fid=req.session['user']).order_by('-id')
    cache.set('arts', Arts)
    return redirect('usercol:whisper')


# 退出
def quit(req):
    req.session.delete()
    return redirect("usercol:index")



# ajax练习
# @csrf_exempt
# def buffer(req):
#     if req.method == 'GET':
#         return render(req,'usercol/balabuffer.html')
#     elif req.method == 'POST':
#         # 用JsonResponse传输数据，方法1
#         # res={}
#         # res['data'] = {'name':'华仔','age':18}
#         # return JsonResponse(res)
#         # 方法2
#         # user = models.Users.usermanage.get(id=1)
#         # # 将对象转为字典
#         # user1 = model_to_dict(user)
#         # print(user1)
#         # return JsonResponse(user1)
#         # 方法3
#         users = models.Users.usermanage.all()
#         # users = serialize('json',users,fields=('username','age'))
#         # return JsonResponse(users,safe=False)
#         users = serialize('json', users)
#         Arts = models.Articles.objects.filter(fid=users)
#         Arts = serialize('json', Arts)
#         return HttpResponse('usercol/register1.html',Arts)

# 保证事务原子性
@transaction.atomic
def reg(req):
    # 设置保存点
    sid = transaction.savepoint()
    try:
        user = models.Users.usermanage.Create_user('qwert', 123456, '123@qq.com')

        transaction.savepoint_commit(sid)
        return HttpResponse('创造完成')
    except:
        transaction.savepoint_rollback(sid)
        return HttpResponse('失败')

