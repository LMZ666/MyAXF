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
    path("market/<int:categoryid>/<int:childtypeid>/",views.market,name="market2"),
    path("market/<int:categoryid>/<int:childtypeid>/<int:sorttype>/",views.market,name="market3")

]