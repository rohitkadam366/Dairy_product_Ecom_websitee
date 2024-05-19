from django.shortcuts import render
from django.views import View
from . models import Product

# Create your views here.
def index(request):
    return render(request, 'app/index.html')


class CategoryView(View):
    def get(self, request,val):
        product=Product.objects.filter(category=val)
        title=Product.objects.filter(category=val).values('title')

        return render(request, 'app/category.html',locals())


class ProductDetail(View):
    def get(self,request,pk):
        return render(request,'app/product_details.html',locals())