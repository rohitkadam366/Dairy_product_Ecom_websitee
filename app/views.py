from django.shortcuts import render,redirect
from django.views import View
from . models import Product,Customer,Cart
from . forms import CustomerRegistrationForm,CustomerLoginForm,CustomerProfileForm,myPasswordChangeForm
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
    add = Customer.objects.filter(user=request.user)
    return render(request,'app/address.html',locals())

class updateaddress(View):
    def get(self,request,pk):
        add = Customer.objects.get(pk=pk)
        form=CustomerProfileForm(instance=add)
        return render(request,'app/updateaddress.html',locals())
    def post(self,request,pk):
        form=CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            user= request.user
            add.name = form.cleaned_data['name']
            add.locality = form.cleaned_data['locality']
            add.city = form.cleaned_data['city']
            add.state = form.cleaned_data['state']
            add.zipcode = form.cleaned_data['zipcode']
            add.save()
            messages.success(request,'Congratulations!! Profile data Update  !!!')
            return redirect('address')
        else:
            messages.error(request,'Invalid Credentials')
            return render(request,'app/updateaddress.html',locals())


def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    print(product_id)
    product = Product.objects.get(id=product_id)
    Cart(user=user,product=product)
    return redirect("/cart")

def show_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    return render(request,'app/addcart.html',locals())




        
    
    























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
        else:
            messages.warning(request,'Please enter correct username and password')
            return render(request,'app/login.html',locals())





















# class password_change_form(View):
#     def get(self,request):
#         form=myPasswordChangeForm()
#         return render(request,'app/password_reset.html',locals())
#     def post(self,request):
#         form=myPasswordChangeForm(request.POST)
#         if form.is_valid():
#             oldpass=form.cleaned_data.get('old_password')
#             newpass=form.cleaned_data.get('new_password1')
#             user=request.user
#             if user.check_password(oldpass):
#                 user.set_password(newpass)
#                 user.save()
#                 messages.success(request,'Password changed successfully')
#                 return redirect('index')
#             else:
#                 messages.warning(request,'Please enter correct old password')
#                 return render(request,'app/password_reset.html',locals())
            

            
# class password_reset(View):
#     def get(self,request):
#         form=mypasswordresetform()
#         return render(request,'app/password_reset.html',locals())
#     def post(self,request):
#         form=mypasswordresetform(request.POST)
#         if form.is_valid():
#             email=form.cleaned_data.get('email')
            
            
    