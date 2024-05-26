from django.contrib import admin
from . models import Product,Customer
# Register your models here.

@admin.register(Product)
class productModelAdmin(admin.ModelAdmin):
    list_display= ['id','title','selling_price','discounted_price','description','composition','prodapp','category']

@admin.register(Customer)
class customerModelAdmin(admin.ModelAdmin):
    list_display= ['id','user','name','locality','city','zipcode','state']
