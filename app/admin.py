from django.contrib import admin
from . models import Product
# Register your models here.

@admin.register(Product)
class productModelAdmin(admin.ModelAdmin):
    list_display= ['id','title','selling_price','discounted_price','description','composition','prodapp','category']