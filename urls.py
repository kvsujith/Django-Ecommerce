from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'shop'

urlpatterns = [
    path('',views.home,name="home"),
    path('cart/<int:id>/<int:userid>',views.cart,name="cart"),
    path('products/<id>',views.products,name="products"),
    path('buy',views.buy,name="buy"),
    path('delete/<int:id>',views.delete,name="delete"),
]
urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)