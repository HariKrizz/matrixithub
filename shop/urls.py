from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name='home'),
    path('<slug:cat_slug>/',views.Home,name='pct_home'),
    path('<slug:cat_slug>/<slug:prd_slug>',views.product_Details,name='details'),
    path('search',views.search,name='search'),
]