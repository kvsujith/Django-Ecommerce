from django.shortcuts import render, redirect
from Products.models import Product,Cart
# Create your views here.
from django.contrib.auth.decorators import login_required




def home(request):
    offers = Product.objects.all().order_by('id')
    return render(request,'index.html',{'offerszone':offers})


@login_required(login_url="/accounts/login")
def cart(request,id,userid):
    print(id,userid)
    prd = Product.objects.get(prdid=id)
    c=Cart(prdid=id,userid=userid,prdname=prd.prdname,prdprice=prd.prdprice,prdimage=prd.prdimage.url)
    c.save()
    return redirect('/buy')



def products(request,id):
    print('id is',id)
    pro =Product.objects.filter(prdcategory__startswith=id).order_by('prdid')

    return render(request,'products.html',{'prods':pro})
@login_required(login_url="/accounts/login")
def buy(request):
    ordersitems = Cart.objects.filter(userid=1)
    print("Names",ordersitems)

    return render(request,'buy.html',{'fstname':'is-valid','lastname':'is-valid','username':'is-valid','orders':ordersitems})

def delete(request,id):
    Cart.objects.get(id=id).delete()

    return redirect('/buy')
