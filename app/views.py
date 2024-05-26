from django.shortcuts import render,redirect
from django.views import View
from . models import Product,Customer
from . forms import CustomerRegistrationForm,CustomerLoginForm,CustomerProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordResetForm
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def about(request):
    return render(request, 'app/about.html')

def contact(request):
    return render(request, 'app/contact.html')


class CategoryView(View):
    def get(self, request,val):
        product=Product.objects.filter(category=val)
        title=Product.objects.filter(category=val).values('title')

        return render(request, 'app/category.html',locals())


class ProductDetail(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        return render(request,'app/product_details.html',locals())
    

class CategoryTitle(View):
    def get(self,request,val):
        product = Product.objects.filter(title=val)
        title = Product.objects.filter(category=product[0].category).values('title')
        return render(request,'app/category.html',locals())
    
class profile_view(View):
    def get(self,request):
        form=CustomerProfileForm()
        return render(request,'app/profile.html',locals())
    def post(self,request):
        form=CustomerProfileForm(request.POST)
        if form.is_valid():
            user= request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user=user,name=name,locality=locality,city=city,state=state,zipcode=zipcode)
            reg.save()
            messages.success(request,'Congratulations!! Profile data Save  !!!')
            return redirect('profile')
        else:
            messages.error(request,'Invalid Credentials')
        return render(request,'app/profile.html',locals())
    
def address(request):
    pass
    
    
    

#############################             Login & Authentication All Method   ############################

class CustomerRegistrationView(View):
    def get(self,request):
        form=CustomerRegistrationForm()
        return render(request,'app/customerregistration.html',locals())
    def post(self,request):
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Congratulations! You have successfully registered')
            return render(request,'app/customerregistration.html',locals())
        else:
            messages.warning(request,'Please fill the form correctly')
            return render(request,'app/customerregistration.html',locals())
        
class Loginview(View):
    def get(self,request):
        form=CustomerLoginForm()
        return render(request,'app/login.html',locals())
    def post(self,request):
        form=CustomerLoginForm(request=request,data=request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get('username')
            upass=form.cleaned_data.get('password')
            user=authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                messages.success(request,'You have successfully logged in')
                return redirect('index')
            else:
                messages.warning(request,'Please enter correct username and password')
                return render(request,'app/login.html',locals())
            
            
# class password_reset(View):
#     def get(self,request):
#         form=mypasswordresetform()
#         return render(request,'app/password_reset.html',locals())
#     def post(self,request):
#         form=mypasswordresetform(request.POST)
#         if form.is_valid():
#             email=form.cleaned_data.get('email')
            
            
    