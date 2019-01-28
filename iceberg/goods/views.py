from django.shortcuts import render, redirect
from . import models
from store.models import stores
from  cars.models import Cars, Orders
from django.core.cache import cache
# Create your views here.


# 上传商品
def upgoods(request):
    if request.method == 'GET':
        return render(request, 'goods/upgoods.html')
    elif request.method=='POST':
        store1 = request.session['store']
        waresname = request.POST['waresname']
        category1 = request.POST['category1']
        category2 = request.POST['category2']
        waresstock = request.POST['waresstock']
        waresprice = request.POST['waresprice']
        waresinfo = request.POST['waresinfo']
        waressize = request.POST['waressize']
        waresprice = float(waresprice)

        ware1 = models.goods(
            waresname=waresname,
            waresstock=waresstock,
            waresprice=waresprice,
            waresinfo=waresinfo,
            waressize=waressize,
            forgoo=store1
            )
        ware1.save()
        categorys = models.category(category1=category1,
                                    category2=category2,
                                    forcat=ware1)
        categorys.save()
        imgstr = ['imag0', 'imag1', 'imag2', 'imag3', 'imag4']
        for i in imgstr:
            try:
                imag0 = request.FILES[i]
                goodsimg = models.goodsimgs(imag0=imag0, forimg=ware1)
                goodsimg.save()
            except:
                pass

            goodsli = models.goods.objects.filter(forgoo=request.session['store'])
            cache.set("goodsli", goodsli)
        # 将商品添加到页面
        goodsall = cache.get('goodsall')
        if goodsall is None:
            stores2 = models.stores.objects.filter(states=True)
            goodsall = []
            for i in stores2:
                goodsall.extend(models.goods.objects.filter(warestatus=True, forgoo=i))
            cache.set('goodsall', goodsall)
        else:
            goodsall.append(ware1)
            cache.set('goodsall', goodsall)
        return render(request, 'store/mystore.html')


# 商家查看商品详情
def detailinfo(request):
    ware1 = models.goods.objects.get(id=int(request.GET['ware1']))
    request.session['ware1'] = ware1
    imgli = models.goodsimgs.objects.filter(forimg=ware1)
    request.session['imgli'] = imgli
    request.session['categorys'] = models.category.objects.get(forcat=ware1)
    return render(request, 'goods/detailinfo.html')


# 商家修改商品信息
def updategoods(request):
    if request.method == 'GET':
        return render(request, 'goods/updategoods.html')
    elif request.method == 'POST':
        waresname = request.POST['waresname']
        waresstock = request.POST['waresstock']
        waresinfo = request.POST['waresinfo']
        waressize = request.POST['waressize']
        waresprice = request.POST['waresprice']

        ware1 = request.session['ware1']
        ware1.waresname = waresname
        ware1.waresstock = waresstock
        ware1.waresinfo = waresinfo
        ware1.waressize = waressize
        ware1.waresprice = waresprice
        ware1.save()
        request.session['ware1'] = ware1
        # 商家修改商品信息，则购物车里信息也做修改
        orders1 = Orders.objects.filter(goodid=ware1.id)
        for i in orders1:
            # 若购物车订单未提交，则修改
            if i.forord.status:
                i.goodname = waresname
                i.goodprice = waresprice
                i.save()
        # 修改图片
        imglis = models.goodsimgs.objects.filter(forimg=ware1)
        imgstr = ['imag0', 'imag1', 'imag2', 'imag3', 'imag4']
        countnum = len(imglis)
        for i in imgstr:
            try:
                imag0 = request.FILES[i]
                goodsimg = models.goodsimgs(imag0=imag0, forimg=ware1)
                goodsimg.save()
                countnum +=1
                if countnum >5 :
                    imglis.first().delete()
            except:
                pass
        return render(request, 'goods/goodsinfo.html')


# 商品的上下架
def updownGoods(request):
    goods1 = models.goods.objects.get(id=int(request.GET['ware']))
    goodsall = cache.get('goodsall')
    if goodsall is None:
        stores2 = models.stores.objects.filter(states=True)
        goodsall = []
        for i in stores2:
            goodsall.extend(models.goods.objects.filter(warestatus=True, forgoo=i))
        cache.set('goodsall', goodsall, 60 * 5)

    if goods1.warestatus:
        goods1.warestatus = False
        # 将商品从页面删除
        if goods1 in goodsall:
            goodsall.remove(goods1)
            cache.set('goodsall', goodsall, 60 * 5)
    else:
        goods1.warestatus = True
        # 将商品添加到页面
        if goods1 not in goodsall:
            goodsall.append(goods1)
            cache.set('goodsall', goodsall, 60 * 5)
    goods1.save()
    goodsli = models.goods.objects.filter(forgoo=request.session['store'])
    cache.set("goodsli", goodsli)
    return redirect('goods:goodsinfo')


# 商家查看商品列表
def goodsinfo(request):
    goodsli = cache.get("goodsli")
    if goodsli is None:
        goodsli = models.goods.objects.filter(forgoo=request.session['store'])
        cache.set("goodsli", goodsli)
    return render(request, 'goods/goodsinfo.html',{'goodsli': goodsli})


# 买家查看商品详情
def single(request):
    ware1 = models.goods.objects.get(id=int(request.GET['seach']))
    request.session['addgoods'] = ware1
    return render(request,'goods/single.html')