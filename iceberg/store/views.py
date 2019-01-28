from django.shortcuts import render, HttpResponse, redirect
from . import models
import hashlib
from django.core.cache import cache
from goods.models import goods,category,cllocter


# 导入分页模块
from django.core.paginator import Paginator
from django.conf import settings
# Create your views here.


# 我的某一个项目
def mystore(request):
    if request.method == 'GET':
        # 传来某一个店铺的id
        if request.GET.get('sid'):
            request.session['store'] = models.stores.objects.get(id=int(request.GET['sid']))
            goodsli = cache.get('goodsli')
            if goodsli is None:
                goodsli = goods.objects.filter(forgoo=request.session['store'])
                cache.set('goodsli', goodsli, 60*5)
        return render(request, 'store/mystore.html')
    elif request.method == 'POST':
        return render(request, 'store/mystore.html')


# 修改店铺信息
def updatestore(request):
    if request.method == 'GET':
        return render(request, 'store/updatestore.html')
    elif request.method == 'POST':
        password = request.POST["password"]
        md = hashlib.md5()
        md.update(password.encode('utf8'))
        pwds = md.hexdigest()
        user = request.session['user']
        if user.pwd != pwds:
            return render(request, 'store/updatestore.html', {'msg': '密码输入错误'})
        storename = request.POST["storename"]
        info = request.POST["info"]
        inlineRadioOptions = request.POST["inlineRadioOptions"]
        # 修改店铺状态
        if inlineRadioOptions == 'True':
            states = True
        elif inlineRadioOptions == 'False':
            states = False
        store2 = request.session['store']
        store2.storename = storename
        store2.storeinfo = info
        store2.states = states
        try:
            storeimg = request.FILES['storeimg']
            store2.storephoto = storeimg
        except:
            pass
        store2.save()
        if inlineRadioOptions != '':
            # 更新页面，避免商店状态的变动导致的错误。

            stores2 = models.stores.objects.filter(states=True)
            goodsall = []
            for i in stores2:
                goodsall.extend(goods.objects.filter(warestatus=True, forgoo=i))
            cache.set("goodsall", goodsall, 60*5)
            temp1 = []
            temp2 = []
            for u in goodsall:
                categorys = category.objects.get(forcat=u)
                if categorys.category1 == '男士':
                    temp1.append(u)
                else:
                    temp2.append(u)
            cache.set('mens', temp1, 60*5)
            cache.set('womens', temp2, 60*5)
        # 更新店铺信息
        request.session['store'] = store2
        store1 = models.stores.objects.filter(masters=request.session['user'])
        request.session['storelis'] = store1
        return render(request, 'store/mystore.html')

# 男装页面
def men(request):
    mens = cache.get("mens")
    if mens is None:
        # 筛选出男/女士商品
        mens = []
        womens = []
        goodsall = cache.get('goodsall')
        if goodsall is None:
            stores2 = models.stores.objects.filter(states=True)
            goodsall = []
            for i in stores2:
                goodsall.extend(goods.objects.filter(warestatus=True, forgoo=i))
            cache.set('goodsall', goodsall, 60 * 5)
        for u in goodsall:
            categorys = category.objects.get(forcat=u)
            if categorys.category1 == '男士':
                mens.append(u)
            else:
                womens.append(u)
        cache.set('mens', mens, 60 * 5)
        cache.set('womens', womens, 60 * 5)
    # 分页
    pagesize = settings.PAGESIZE
    paginator = Paginator(mens, pagesize + 2)
    # 获取当前页的页码
    pagenum = request.GET.get('pagenum', default=1)
    page = paginator.page(int(pagenum))
    return render(request, 'store/men.html', {'paginator':paginator, 'page':page})

# 女装页面
def women(request):
    womens = cache.get('womens')
    if womens is None:
        # 筛选出男/女士商品
        mens = []
        womens = []
        goodsall = cache.get('goodsall')
        if goodsall is None:
            stores2 = models.stores.objects.filter(states=True)
            goodsall = []
            for i in stores2:
                goodsall.extend(goods.objects.filter(warestatus=True, forgoo=i))
            cache.set('goodsall', goodsall, 60 * 5)
        for u in goodsall:
            categorys = category.objects.get(forcat=u)
            if categorys.category1 == '男士':
                mens.append(u)
            else:
                womens.append(u)
        cache.set('mens', mens, 60 * 5)
        cache.set('womens', womens, 60 * 5)
    # 分页
    pagesize = settings.PAGESIZE
    paginator = Paginator(womens, pagesize+2)
    # 获取当前页的页码
    pagenum = request.GET.get('pagenum', default=1)
    page = paginator.page(int(pagenum))
    return render(request, 'store/women.html', {'paginator':paginator, 'page': page})


# 收藏页面
def collection(request):
    # 判断有没有登陆
    if 'user' not in request.session:
        return redirect('users:logins')
    colllist = cllocter.objects.filter(forcll=request.session['user'])
    request.session['colllist'] = []
    for i in colllist:
        wares1 = goods.objects.get(id=i.goodsid)
        request.session['colllist'].append(wares1)
    return render(request, 'store/collection.html')


def addcollect(request,id):
    # 判断有没有登陆
    if 'user' not in request.session:
        return redirect('users:logins')
    # 添加收藏
    clllos1 = cllocter.objects.filter(goodsid=id, forcll=request.session['user'])
    if not clllos1.exists():
        cllos = cllocter(goodsid=id, forcll=request.session['user'])
        cllos.save()
        mas = '收藏成功'
    else:
        mas = '收藏库已有该商品'
    return HttpResponse(mas)


def colldel(request):
    # 取消收藏
    sid = request.GET['seach']
    clllos = cllocter.objects.get(goodsid=sid, forcll=request.session['user'])
    clllos.delete()
    return redirect('store:collection')
