from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.sessions.models import Session
from .models import *
from shop.models import *
from django.core.exceptions import ObjectDoesNotExist
import datetime
from datetime import timedelta

# Create your views here.
def cart_details(request, total=0, count=0, crt_items=None):
    try:   
        crt_lst = cartList.objects.get(cart_id=crt_id(request)) 
        crt_items = cartItems.objects.filter(cart=crt_lst, active=True)

        for i in crt_items:
            total += (i.prod.price * i.qty)
            count += i.qty
    except ObjectDoesNotExist:
        pass
    return render(request,'Cart.html', {'crt_items':crt_items, 'c_tot':total, 'count':count})

def crt_id(request):
    c_id = request.session.session_key
    if not c_id:
        c_id = request.session.create
    return c_id

def user_session(request):
    usr_sid = request.session.session_key
    if not usr_sid:
        usr_sid = request.session.create
    return usr_sid

def add_Cart(request,prdct_id):
    product = Product.objects.get(id=prdct_id)
    
    try:
        crt_lst = cartList.objects.get(cart_id=crt_id(request),user_id=user_session(request))  

    except cartList.DoesNotExist:
        crt_lst = cartList.objects.create(cart_id=crt_id(request),user_id=user_session(request))
        crt_lst.save()
    
    try:
        crt_items = cartItems.objects.get(prod=product,cart=crt_lst)
        if crt_items.qty < crt_items.prod.stock:
            crt_items.qty += 1
        crt_items.save()
    except cartItems.DoesNotExist:
        crt_items = cartItems.objects.create(prod=product,qty=1,cart=crt_lst)
        crt_items.save()
        
    return redirect('cart_details')

def decr_Cart(request,prdct_id):
    ct_item = cartList.objects.get(cart_id=crt_id(request),user_id=user_session(request))  
    prodct = get_object_or_404(Product,id=prdct_id)
    cart_items = cartItems.objects.get(prod=prodct,cart=ct_item)

    if cart_items.qty > 1:
        cart_items.qty -= 1
        cart_items.save()
    else:
        cart_items.delete()
    return redirect('cart_details')

def del_Cart(request,prdct_id):
    ct_item = cartList.objects.get(cart_id=crt_id(request),user_id=user_session(request))   
    prodct = get_object_or_404(Product,id=prdct_id)
    cart_items = cartItems.objects.get(prod=prodct,cart=ct_item)
    cart_items.delete()

    return redirect('cart_details')

def buy_Cart(request,prdct_id,tot=0): 
    ct_item = cartList.objects.get(cart_id=crt_id(request),user_id=user_session(request))  
    prodct = get_object_or_404(Product,id=prdct_id)
    cart_items = cartItems.objects.get(prod=prodct,cart=ct_item)
    tot += prodct.price * cart_items.qty
  
    return render(request, 'Payment.html', {'total': tot})

def confirm_Payment(request):
 
    now = datetime.date.today()
    delivery_date = str(now + timedelta(weeks=1, days=2))                                                                                                                                                                                                              

    if request.method == 'POST':
        name = request.POST["Name"]
        cardnum = request.POST["cardNumber"]
        expmnth = int(request.POST['month'])
        expyear = request.POST["year"]
        cvv = str(request.POST["cvv"])

        if len(cvv) > 3:
            messages.info(request,"Please enter a valid CVV")  
            return redirect('cart_details')

        if expmnth < 1 or expmnth > 12:
            messages.info(request,"Please enter a valid month!")
            return redirect('cart_details') 

        else:
            messages.info(request,"Your order is complete!. The product will be Delivered by: "+ delivery_date)
            return redirect('cart_details')         
    else:
        return render(request,'Payment.html')