from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'shop'

urlpatterns = [
    path('',views.home,name="home"),
    path('cart/<int:id>',views.cart,name="cart"),
    path('cartPage',views.cartPage,name="cartPage"),
    path('products/<id>',views.products,name="products"),
    path('buy',views.buy,name="buy"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('reduce/<int:id>',views.reduce,name="reduce"),
    path('increase/<int:id>',views.increase,name="increase"),
    path('abc',views.ProductDetailView.as_view(),name="abc"),

]
urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)