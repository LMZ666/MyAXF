from django.shortcuts import render

# Create your views here.
from App.models import Wheel, Nav, Mustbuy, Shop, MainShop, Foodtypes, Goods


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


def market(request,categoryid=0,childtypeid=0,sorttype=0):
    foodtypes = Foodtypes.objects.all()
    if categoryid == 0:
        categoryid = foodtypes.first().typeid
    foodtype = Foodtypes.objects.get(typeid=categoryid)
    # 当我们传递两个有关联的值时，可以使用数组嵌套字典的形式
    # 这样方便了在模板中取值
    typeidnamelist=list()
    for type in foodtype.childtypenames.split("#"):
        typeidname={
            "typeid":type.split(":")[1],
            "typename":type.split(":")[0]
        }
        typeidnamelist.append(typeidname)

    # 商品的筛选
    if childtypeid==0:
        goods =Goods.objects.filter(categoryid=categoryid)
    else:
        goods = Goods.objects.filter(categoryid=categoryid,childcid=childtypeid)
    if sorttype==2:
        goods = goods.order_by("productnum")
    elif sorttype==3:
        goods = goods.order_by("price")
    elif sorttype==4:
        goods = goods.order_by("-price")

    data = {
        "foodtypes": foodtypes,
        "goods": goods,
        "categoryid":categoryid,
        "typeidnamelist":typeidnamelist,
        "childtypeid":childtypeid,
    }
    return render(request, "market/market.html", context=data)