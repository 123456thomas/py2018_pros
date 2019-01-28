from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import hashlib


from . import models

def Bockemain(request):
    return HttpResponse("Bocke")

# Create your views here.
def Create_author(request):
    # 方法一
    # author=models.Users.Create("Tom",'123456')
    # 方法二：对象属性操作方式
    # author = models.Users(username="Jim",'123456')
    # 方法三：类管理器
    try:
        # 增加用户
        author = models.Users.usermanage.create_user(name="bcbtg1",id=5)
        author.save()
        return HttpResponse("Save OK")
    except Exception as e:
        return HttpResponse("该用户已存在")


# 查看一个
def find(request):
    # 查看所有用户
    try:
        infoall = models.Users.usermanage.getone(3)
        print(infoall)
        return HttpResponse(infoall)
    except:
        return HttpResponse("该用户不存在")

# 查看所有
def findall(request):
    # 查看所有用户
    infoall = models.Users.usermanage.findall()
    print(infoall)
    return HttpResponse(infoall)


# 删除数据
def delete(request):
    models.Users.usermanage.delone(3)
    return HttpResponse('删除成功')


# 修改数据
def update(request):
    user = models.Users.usermanage.update(6,"yuo")
    user.save()
    return HttpResponse('<h1 align="center">修改成功</h1>')


# rest参数传递
def param(request,name):
    print(name)
    return HttpResponse(name)


# rest参数传递
def param2(request,num):
    print(num)
    return HttpResponse(num)


# rest参数传递
def params(request,username):
    print(username)
    print(request.path, request.method)
    return HttpResponse(username)

# 查看request 的一些属性
def reqmeth(request):
    print(request.path)
    print(request.method)
    print(request.GET['name'])  #或print(request.GET.get('name')
    print(request.path)
    print(request.encoding)


# 视图跳转，方法一：
def index1(req):
    temp = loader.get_template("Bocke/index1.html")    # 二级目录名字和应用一致
    context = {"msg": "华仔"}
    return HttpResponse(temp.render(context, req))


# 视图跳转，方法二：
def index2(req):
    context2 = {"msg": "华欣"}
    return HttpResponse(render( req,"Bocke/index1.html",context2))


def index(req):
    context2 = {"msg": "华欣"}
    return HttpResponse(render( req,"Bocke/index1.html"))


def login(req):
    return HttpResponse(render( req,"Bocke/register.html"))


def logsend(req):
    name = req.POST["username"]
    u=models.Users.usermanage

    # 查看用户名是否存在
    if u.filter(username=name).exists():
        user = u.get(username=name)
        pwd = user.pwd
        print(req.POST["pwd"])
        # 查看密码是否正确
        md = hashlib.md5()
        md.update(req.POST["pwd"].encode("utf8"))
        pwds = md.hexdigest()
        if pwd == pwds:
            au = models.Artiles.artmanage
            arts = au.filter(author_id=user.id)
            print(arts)
            return HttpResponse(render(req, "Bocke/login_success.html",{"user":user,"arts":arts,"sum":len(arts)}))
        else:
            return HttpResponse(render(req, "Bocke/register.html", {"msg": "密码错误"}))
    else:
        return HttpResponse(render(req, "Bocke/register.html",{"msg":"该用户不存在"}))


# 注册
def register(req):
        return HttpResponse(render(req, "Bocke/register.html"))


# 注册响应
def registsend(req):
    name = req.POST["username"]
    u = models.Users.usermanage
    pwd = req.POST["pwd"]
    print(type(req.POST["age"]), str(req.POST["age"]))
    if len(str(req.POST["age"]))>0:
        age = int(req.POST["age"])
    else:
        age = 18  # 默认18岁

    if len(pwd) not in range(8,17):
        return render(req, "Bocke/register.html", {"msg": "密码格式错误"})
    elif len(name) not in range(3,9):
        return render(req, "Bocke/register.html", {"msg": "名字格式错误"})
    elif age not in range(8, 120):
        return render(req, "Bocke/register.html", {"msg": "年龄错误"})
    else:
        if u.filter(username=name).exists():
            return render(req, "Bocke/register.html", {"msg": "该用户已存在，请重新注册"})
        else:
            md = hashlib.md5()
            md.update(pwd.encode("utf8"))
            pwd1 = md.hexdigest()
            authr = u.create(username=name, pwd=pwd1, age=age)
            authr.save()
            return render(req, "Bocke/regist_success.html")


# 模块
def index0(re):
    user = models.Users.usermanage.get(id=1)
    # user = models.Users.usermanage.filter(id=1).first()

    return render(re,"main.html",{"user":user})


# 写文章
def logsuccess(ref):
    title = ref.POST["title"]
    auth = ref.POST["auth"]
    con = ref.POST["con"]
    user=models.Users.usermanage.filter(id=int(auth)).first()
    wd = models.Artiles.artmanage.Writeart(title,con,user)
    au = models.Artiles.artmanage
    arts = au.filter(author_id=auth)
    print(arts)
    return render(ref, "Bocke/login_success.html",{"arts":arts,"sum":len(arts),"user":user})

def writing(ref):
    return render(ref, "Bocke/writing.html")
# 读文章

def read(ref):
    content = ref.POST["con"]
    ctime = ref.POST["ct"]
    author = ref.POST["author"]
    title = ref.POST["atitle"]
    print(author)
    return render(ref, "Bocke/readbocke.html",{"content":content,"ctime":ctime,"title":title,"author":author})