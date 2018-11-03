from django.shortcuts import render

# Create your views here.
from App.models import Wheel, Nav, Mustbuy, Shop, MainShop


def home(request):
    # 轮播图数据
    wheels = Wheel.objects.all()

    # 导航数据
    navs = Nav.objects.all()

    # 每日必购
    mustbuys = Mustbuy.objects.all()

    shops = Shop.objects.all()
    # 商品头部
    shophead = shops[0]
    shoptab = shops[1:3]
    shopclass = shops[3:7]
    shopcommend = shops[7:]
    mainshow = MainShop.objects.all()

    data = {
        "wheels": wheels,
        "navs": navs,
        "mustbuys": mustbuys,
        "shophead":shophead,
        "shoptab":shoptab,
        "shopclass":shopclass,
        "shopcommend":shopcommend,
        "mainshow":mainshow

    }
    return render(request, "home/home.html",context=data)


def base(request):
    return render(request, "base/base.html")


def cart(request):
    return render(request, "cart/cart.html")


def mine(request):
    return render(request, "mine/mine.html")


def market(request):
    return render(request, "market/market.html")