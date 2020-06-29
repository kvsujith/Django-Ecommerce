from django.contrib import admin

from .models import Products,Cart,OrderedItems
# Register your models here.
admin.site.register(Products)
admin.site.register(Cart)
admin.site.register(OrderedItems)



