from django.urls import path
from . import views

urlpatterns = [
    path('cart_details',views.cart_details,name='cart_details'),
    path('add_Cart/<int:prdct_id>',views.add_Cart,name='add_Cart'),
    path('decr_Cart/<int:prdct_id>',views.decr_Cart,name='decr_Cart'),
    path('del_Cart/<int:prdct_id>',views.del_Cart,name='del_Cart'),
    path('cart_Buy/<int:prdct_id>',views.buy_Cart,name='buy_Cart'),
    path('cart_Buy/confirm_pay',views.confirm_Payment,name='confirm_pay')
]