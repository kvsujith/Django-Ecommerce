from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.utils.datetime_safe import datetime
from django.views.generic import DetailView
from Products.models import Products, Cart,OrderedItems
from django.contrib.auth.decorators import login_required


# Create your views here.


def home(request):
    offers = Products.objects.all().order_by('id')
    return render(request, 'index.html', {'offerszone': offers})


def products(request, id):
    print('id is', id)
    pro = Products.objects.filter(prdcategory__startswith=id).order_by('prdid')
    return render(request, 'products.html', {'prods': pro})


@login_required(login_url="/accounts/login")
def cart(request, id):
    print(id, request.user.id)
    if Cart.objects.filter(products_id=id, userid=request.user.id).exists():
        # we get a match from Cart Model
        print("Products id and user id is matched")
        f = Cart.objects.filter(products_id=id, userid=request.user.id)
        print("this is id", f)
        e = Cart.objects.get(pk=f[0].id)
        print("This is inside")
        print(f)
        e.qty += 1
        e.save()
        messages.info(request, "Cart Updated")
        return redirect('/#offerszone')
    else:
        prd = Products.objects.get(prdid=id)
        c = Cart(prdid=id, userid=request.user.id, prdname=prd.prdname, prdprice=prd.prdprice,
                 prdimage=prd.prdimage.url, products_id=id)
        c.save()
        print("====Added to Cart======")
        messages.info(request, "Added to Cart")
        return redirect('/#offerszone')
    return redirect(f'/cartPage/{request.user.id}')


@login_required(login_url="/accounts/login")
def reduce(request, id):
    print("user id without url", request.user.id)
    c = Cart.objects.get(pk=id)
    c.qty -= 1
    if c.qty < 1:
        messages.info(request, "Minimum Qty 1 should mainatain")
        return redirect('/buy')
    else:
        c.save()
    return redirect('/buy')


def increase(request, id):
    c = Cart.objects.get(pk=id)
    c.qty += 1
    c.save()
    return redirect('/buy')


@login_required(login_url="/accounts/login")
def cartPage(request):
    context = {}
    cart = Cart.objects.filter(userid=request.user.id)
    print(cart, "This is from cartPage")
    context['items'] = cart
    return render(request, 'cart.html', context)


@login_required(login_url="/accounts/login")
def buy(request):
    ordersitems = Cart.objects.filter(userid=request.user.id).order_by('-id')
    subtotal=0
    for i in ordersitems:
        subtotal += i.get_price()

    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        mob1 = request.POST['mob1']
        mob2 = request.POST['mob2']
        location = request.POST['location']
        address = request.POST['address']
        zipcode = request.POST['zipcode']
        items=[x for x in ordersitems]
        print(items)
        for i in items:
            print(i.prdid,i.prdname,i.userid,i.prdprice,i.qty,i.get_price())
            user = OrderedItems.objects.create(prdid=i.prdid,userid=request.user.id,prdname=i.prdname,price=i.prdprice,qty=i.qty,
                                               username=request.user.username,mob1=mob1,mob2=mob2,location=location,DeliveryAddress=address,zipCode=zipcode,
                                               DateofOrdered=datetime.now(),Delivery_Charge=50,Discount=100,cart_id=i.id,totalAmount=i.get_price())
            user.save()
        print([fname, lname, mob1, mob2, location, address, zipcode])
        return redirect('/')

    return render(request, 'buy.html', {'orders': ordersitems,'subtotal':subtotal,'delivery':50,'discount':10,'grandtotal':((subtotal+50)-10) })

def delete(request, id):
    Cart.objects.get(id=id).delete()
    return redirect('/buy')


class ProductDetailView(LoginRequiredMixin, DetailView):
    login_url = '/accounts/register'
    model = Products.objects.get(pk=1)
    template_name = "prddetailview.html"
    context_object_name = "abc"

    def get_object(self, queryset=None):
        return self.model
