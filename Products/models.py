from django.db import models

# Create your models here.

CATEGORIES = (
    ('Vegetables', 'Vegetables'),
    ('Grocery', 'Grocery'),
    ('Stationary', 'Stationary'),
    ('Fruits', 'Fruits'))
prditemstype = (
    ('Kg', 'kilogram'),
    ('Ltr', 'Litre'),
    ('pcs', 'Piece'),
    ('pack', 'Pack'),
    ('bundle', 'Bundle'))


class Products(models.Model):
    prdid = models.CharField(max_length=6)
    prdname = models.CharField(max_length=50)
    prdcategory = models.CharField(max_length=30, choices=CATEGORIES, default='Vegetables')
    prditemstypes = models.CharField(max_length=30, choices=prditemstype, default='Kg')
    prdimage = models.ImageField(upload_to='picturess')
    prdstock = models.IntegerField()
    prdqtytype = models.CharField(max_length=10)
    prdprice = models.CharField(max_length=10)
    prdoffer = models.BooleanField(default=False)
    prdofferprice = models.CharField(max_length=10)

    def __str__(self):
        return '{}'.format(self.prdname)


class Cart(models.Model):
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    prdid = models.CharField(max_length=6)
    userid = models.CharField(max_length=50)
    prdname = models.CharField(max_length=50)
    prdimage = models.CharField(max_length=50)
    prdprice = models.IntegerField(default=0)
    qty = models.IntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.prdname)

    def get_price(self):
        return self.qty * self.prdprice

    def get_total(self):
        total = 0
        for i in Cart.objects.all():
            total += i.get_price()
        return total


class OrderedItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    prdid = models.IntegerField()
    userid = models.IntegerField()
    prdname = models.CharField(max_length=20)
    qty = models.IntegerField()
    price = models.IntegerField()
    totalAmount = models.IntegerField(default=0)
    DateofOrdered = models.DateTimeField()
    Delivery_Charge = models.IntegerField()
    Discount = models.FloatField()
    username = models.CharField(max_length=20)
    mob1 = models.CharField(max_length=10)
    mob2 = models.CharField(max_length=10)
    location = models.CharField(max_length=10)
    DeliveryAddress = models.CharField(max_length=50)
    zipCode = models.CharField(max_length=6)

    def __str__(self):
        return '{}'.format(self.prdname)
