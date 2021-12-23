from . models import *
from . views import *

def count(request): 
   #user logout 
   item_count = 0

   if 'admin' in request.path:
      return {}
   else:
      try:
         ct = cartList.objects.filter(cart_id=crt_id(request))    
         ct_items = cartItems.objects.all().filter(cart=ct[:1])

         for i in ct_items:
            item_count += i.qty
      except cartList.DoesNotExist:
         item_count = 0
      return dict(itc=item_count) 