from django.contrib import admin
from . models import *

# Register your models here.
class categ_admin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('cat_name',)}
admin.site.register(Category,categ_admin)

class prod_admin(admin.ModelAdmin):
    list_display = ['id','name','slug','price','stock','image','avail','desc',]    # To view the data in Admin Panel
    list_editable = ['price','stock','image','desc','avail']                 # Edit data from view in Admin 
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Product,prod_admin)