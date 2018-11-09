from django.db import models

# 基础类
class Base(models.Model):
    # 图片
    img = models.CharField(max_length=100)
    # 名称
    name = models.CharField(max_length=100)
    # 商品编号
    trackid = models.CharField(max_length=10)

    class Meta:
        abstract = True


# 轮播图
class Wheel(Base):
    class Meta:
        db_table = 'axf_wheel'

# 导航
class Nav(Base):
    class Meta:
        db_table = 'axf_nav'

# 每日必购
class Mustbuy(Base):
    class Meta:
        db_table = 'axf_mustbuy'
# 商品
class Shop(Base):
    class Meta:
        db_table = 'axf_shop'

#insert into axf_mainshow(trackid,name,img,categoryid,brandname,img1,childcid1,productid1,longname1,price1,marketprice1,img2,childcid2,productid2,longname2,price2,marketprice2,img3,childcid3,productid3,longname3,price3,marketprice3)
class MainShop(models.Model):
    trackid = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    img = models.CharField(max_length=100)
    categoryid = models.CharField(max_length=10)
    brandname = models.CharField(max_length=20)
    img1 = models.CharField(max_length=100)
    childcid1 = models.CharField(max_length=10)
    productid1 = models.CharField(max_length=10)
    longname1 = models.CharField(max_length=50)
    price1 = models.CharField(max_length=100)
    marketprice1 = models.CharField(max_length=100)
    img2 = models.CharField(max_length=100)
    childcid2 = models.CharField(max_length=100)
    productid2 = models.CharField(max_length=100)
    longname2 = models.CharField(max_length=100)
    price2 = models.CharField(max_length=100)
    marketprice2 = models.CharField(max_length=100)
    img3 = models.CharField(max_length=100)
    childcid3 = models.CharField(max_length=100)
    productid3 = models.CharField(max_length=100)
    longname3 = models.CharField(max_length=100)
    price3 = models.CharField(max_length=100)
    marketprice3 = models.CharField(max_length=100)
    class Meta:
        db_table="axf_mainshow"

# typeid,typename,childtypenames,typesort
class Foodtypes(models.Model):
    typeid = models.CharField(max_length=10)
    typename = models.CharField(max_length=20)
    childtypenames = models.CharField(max_length=256)
    typesort = models.IntegerField()
    class Meta:
        db_table="axf_foodtypes"

#productid,productimg,productname,productlongname,isxf,pmdesc,specifics,price,marketprice,categoryid,childcid,childcidname,dealerid,storenums,productnum
class Goods(models.Model):
    productid = models.CharField(max_length=10)
    productimg = models.CharField(max_length=100)
    productname = models.CharField(max_length=50)
    productlongname = models.CharField(max_length=100)
    isxf = models.IntegerField()
    pmdesc = models.IntegerField()
    specifics = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    marketprice = models.DecimalField(max_digits=12,decimal_places=6)
    categoryid = models.IntegerField()
    childcid = models.IntegerField()
    childcidname = models.CharField(max_length=10)
    dealerid = models.CharField(max_length=10)
    storenums = models.IntegerField()
    productnum = models.IntegerField()
    class Meta:
        db_table = "axf_goods"

class User(models.Model):
    name = models.CharField(max_length=30)
    account = models.CharField(max_length=20,unique=True)
    password = models.CharField(max_length=256)
    token = models.CharField(max_length=256)
    img = models.CharField(max_length=200,default="/static/mine/img/default.jpg")
    rank = models.CharField(max_length=10,default=1)

    class Meta:
        db_table="axf_user"

class Carts(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods,on_delete=models.CASCADE)
    num = models.IntegerField()
    isselect = models.BooleanField(default=True)
    class Meta:
        db_table = "axf_carts"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    createtime = models.DateTimeField(auto_now_add=True)
    # 状态
    # -1 过期
    # 1 未付款
    # 2 已付款，未发货
    # 3 已发货，快递
    # 4 已签收，未评价
    # 5 已评价
    # 6 退款....
    status = models.IntegerField(default=1)
    # 订单号
    identifier = models.CharField(max_length=100)

    class Meta:
        db_table = "axf_order"


class OrderGoods(models.Model):
    # 用来连接商品和订单之间的关系
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    num = models.IntegerField()

    class Meta:
        db_table = "axf_ordergoods"











