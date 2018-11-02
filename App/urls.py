from django.urls import path

from App import views

urlpatterns = [
    path("base/", views.base, name="base"),
    path("", views.home, name="home"),
    path("cart/", views.cart, name="cart"),
    path("mine/", views.mine, name="mine"),
    path("market/", views.market, name="market")
]