import os
import random
import uuid
import time

from PIL import Image, ImageDraw, ImageFont
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from App.models import Wheel, Nav, Mustbuy, Shop, MainShop, Foodtypes, Goods, User, Carts, Order, OrderGoods


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
        "shophead": shophead,
        "shoptab": shoptab,
        "shopclass": shopclass,
        "shopcommend": shopcommend,
        "mainshow": mainshow

    }
    return render(request, "home/home.html", context=data)


# 检测账号是否存在


def base(request):
    return render(request, "base/base.html")


# 购物车
def cart(request):
    token = request.session.get("token")
    try:
        user = User.objects.get(token=token)
        carts = Carts.objects.filter(user=user)
        money = 0
        carts1 = Carts.objects.filter(user=user,isselect=1)

        for cart in carts1:
            money += cart.goods.marketprice*cart.num
        money = round(money,2)
        data = {
            "carts": carts,
            "money":money
        }
        return render(request, "cart/cart.html",context=data)
    except:

        return redirect("app:login")

# 获取总钱数
def getMoney(request):
    token = request.session.get("token")
    cartid = request.GET.get("cartid")
    cart = Carts.objects.get(pk=cartid)
    cart.isselect = not(cart.isselect)
    isselect = cart.isselect
    print(cart.isselect)
    print(isselect,cartid)
    cart.save()
    user = User.objects.get(token=token)
    carts = Carts.objects.filter(isselect=1, user=user)
    # money =
    money = 0
    for cart in carts:
        money += cart.goods.marketprice*cart.num
    #     保留两位小数
    money = round(money,2)
    print(money)
    data={
        "msg":"选择",
        "status":1,
        "money":money,
        "isselect":isselect
    }
    return JsonResponse(data)

def selectAll(request):
    token = request.session.get("token")
    user = User.objects.get(token=token)
    carts = Carts.objects.filter(user=user)
    money = 0
    if request.GET.get("isselect")=="1":
        for cart in carts:
            cart.isselect = 1
            cart.save()
            money += cart.goods.marketprice*cart.num
    else:
        for cart in carts:
            cart.isselect = 0
            cart.save()
    money=round(money,2)
    data = {
        "money": money
    }
    return JsonResponse(data)

# 我的
def mine(request):
    token = request.session.get("token")
    print(token)
    data = {
        "islogin": 0
    }
    if token:
        try:
            user = User.objects.get(token=token)
            print(user)
            data["user"] = user
            data["islogin"] = 1
            return render(request, "mine/mine.html", context=data)
        except:
            return render(request, "mine/mine.html")

    return render(request, "mine/mine.html")


# 商品分类展示,同时传递用户的商品信息过去
def market(request, categoryid=0, childtypeid=0, sorttype=0):
    foodtypes = Foodtypes.objects.all()
    if categoryid == 0:
        categoryid = foodtypes.first().typeid
    foodtype = Foodtypes.objects.get(typeid=categoryid)
    # 当我们传递两个有关联的值时，可以使用数组嵌套字典的形式
    # 这样方便了在模板中取值
    typeidnamelist = list()
    for type in foodtype.childtypenames.split("#"):
        typeidname = {
            "typeid": type.split(":")[1],
            "typename": type.split(":")[0]
        }
        typeidnamelist.append(typeidname)

    # 商品的筛选
    if childtypeid == 0:
        goods = Goods.objects.filter(categoryid=categoryid)
    else:
        goods = Goods.objects.filter(categoryid=categoryid, childcid=childtypeid)
    if sorttype == 2:
        goods = goods.order_by("productnum")
    elif sorttype == 3:
        goods = goods.order_by("price")
    elif sorttype == 4:
        goods = goods.order_by("-price")
    token = request.session.get("token")
    try:
        user = User.objects.get(token=token)
        # 得到该用户对应的所有商品
        carts = Carts.objects.filter(user=user)
    except:
        carts = None
    data = {
        "foodtypes": foodtypes,
        "goods": goods,
        "categoryid": categoryid,
        "typeidnamelist": typeidnamelist,
        "childtypeid": childtypeid,
        "carts":carts
    }
    return render(request, "market/market.html", context=data)


# 注册
def register(request):
    user = User()
    if request.method == "POST":
        user.name = request.POST.get("name")
        user.account = request.POST.get("account")
        user.password = request.POST.get("passwd")
        user.token = str(uuid.uuid5(uuid.uuid4(), user.name))
        imgname = str(uuid.uuid4())
        path = "static/mine/img/upload/" + imgname + ".png"
        files = request.FILES.get("img")
        user.img = "/" + path
        with open(path, "wb") as fp:
            for file in files.chunks():
                fp.write(file)
        print(user.name, user.account, user.token)
        user.save()
        request.session["token"] = user.token
        return redirect("app:mine")
    else:
        return render(request, "mine/register.html")


# 图形验证码
def imgCheck(requset):
    if len(os.listdir("static/mine/img/check")) > 5:

        file_list = os.listdir("static/mine/img/check")
        for file in file_list:
            os.remove(os.path.join("static/mine/img/check", file))
    num = random.randrange(100000)
    path = "static/mine/img/check/" + str(num) + ".png"
    width = 90
    height = 40
    color = (random.randrange(256), random.randrange(256), random.randrange(256))
    image = Image.new("RGB", (width, height), color)
    # 画出了一张图片
    draw = ImageDraw.Draw(image)
    # 添加噪点
    for i in range(200):
        xy = (random.randrange(100), random.randrange(50))
        color = (random.randrange(256), random.randrange(256), random.randrange(256))
        draw.point(xy, fill=color)

    # 获取到字体  有的字体会用不了，如果没有显示出文字就换个字体
    font = ImageFont.truetype("static/font/QingShu.ttf", 40)
    str1 = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    text = ""
    for i in range(4):
        color = (255, random.randrange(256), random.randrange(256))
        num = str1[random.randrange(len(str1))]
        text += num
        # 第一个参数是距离left，第二个是top
        draw.text((5 + i * 20, 2), num, fill=color, font=font)

    if os.path.exists(path):
        os.remove(path)
    image.save(path)
    response = HttpResponse(path)
    # max_age和expires都是指定时间，max_age指定秒数，expires指定天数
    response.set_cookie("imgcode", text, max_age=60 * 10)
    return response


# 验证账号是否存在
def account(request):
    responseData = {}
    account = request.GET.get("account")
    try:
        User.objects.get(account=account)
        responseData['status'] = 0
        # print("用户已经注册")
    except:
        # print("用户未注册")
        responseData['status'] = 1

    return JsonResponse(responseData)


#
def login(request):
    if request.method == "POST":
        account = request.POST.get("account")
        passwd = request.POST.get("passwd")
        try:
            user = User.objects.get(account=account, password=passwd)
            user.token = str(uuid.uuid5(uuid.uuid4(), user.name))
            request.session["token"] = user.token
            user.save()
            print(user.token)
            return redirect("app:mine")
        except:
            print("登录失败！！！！！！！")

    return render(request, "mine/login.html")


def logout(request):
    request.session.flush()
    response = redirect("app:mine")
    return response

def addcart(request):
    goodid = request.GET.get("goodid")
    goods = Goods.objects.get(pk=goodid)
    token = request.session.get("token")
    try:
        user = User.objects.get(token=token)
    except:
        return JsonResponse({"login":0})
    try:
        cart = Carts.objects.get(goods=goods,user=user)
        cart.num = cart.num+1
        cart.save()
    except:
        cart = Carts()
        cart.goods = goods
        cart.user = user
        cart.num = 1
        cart.save()
    #   报错  Carts' is not JSON serializable
    #   意思是carts对象不能进行json序列化
    data={
        "msg":"添加成功",
        "status":1,
        "cartnum":cart.num
    }
    print(cart.num)
    return JsonResponse(data)



def minusCart(request):


    # 在减号出现的条件下就代表了用户已经登录，并且商品数目也是已经大于1
    goodid = request.GET.get("goodid")
    goods = Goods.objects.get(pk=goodid)
    token = request.session.get("token")
    user = User.objects.get(token=token)
    cart = Carts.objects.get(goods=goods,user=user)
    cart.num-=1
    cart.save()
    data={
        "msg":"减少商品",
        "status":1,
        "cartnum":cart.num
    }
    if cart.num==0:
        cart.delete()
    return JsonResponse(data)


def makeOrder(request):
    token = request.session.get("token")
    user = User.objects.get(token=token)
    order = Order()
    order.user = user  # 绑定用户了
    order.identifier = str(int(time.time())+random.randrange(10000,100000))
    carts = Carts.objects.filter(user=user,isselect=1)
    order.save()
    print(carts)
    # 绑定商品和商品数目
    for cart in carts:
        print(cart.goods)
        # 使得所有的ordergoods都和同一个order绑定
        ordergoods = OrderGoods()
        ordergoods.order = order
        # 每一个ordergoods都绑定了一个商品
        ordergoods.goods = cart.goods
        ordergoods.num = cart.num
        ordergoods.save()
        # 通过这样的中间关系，我们实现了一个order中对应了多个goods

    return HttpResponse(order)

def order(request):
    token = request.session.get("token")
    user = User.objects.get(token=token)
    orders = Order.objects.filter(user=user)

    data={
        "orders":orders
    }
    return render(request,"order/order.html",data)
