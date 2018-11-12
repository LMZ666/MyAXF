from django.urls import path
from App import views
urlpatterns = [
    path("base/", views.base, name="base"),
    path("", views.home, name="home"),
    path("cart/", views.cart, name="cart"),
    path("mine/", views.mine, name="mine"),
    path("market/", views.market, name="market"),
    # 此处的参数要和函数的参数名称相同
    path("market/<int:categoryid>/", views.market, name="market1"),
    path("market/<int:categoryid>/<int:childtypeid>/", views.market, name="market2"),
    path("market/<int:categoryid>/<int:childtypeid>/<int:sorttype>/", views.market, name="market3"),
    path("register/", views.register, name="register"),
    path("imgcheck/", views.imgCheck, name="imgcheck"),
    path("account/", views.account),
    path("login/", views.login, name="login"),
    path("logout/",views.logout,name="logout"),
    path("addcart/", views.addcart),
    path("minuscart/",views.minusCart),
    path("order/",views.order,name="order"),
    path("makeorder/",views.makeOrder),
    path("getmoney/",views.getMoney,name="getmoney"),
    path("selectall/",views.selectAll),
    path("notifyurl/",views.notifyurl,name="notifyurl"),
    path("pay/",views.pay),
    path("retrunurl/",views.returnurl,name="returnurl")
]