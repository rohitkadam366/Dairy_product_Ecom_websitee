from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from . forms import mypasswordresetform,myPasswordChangeForm,mysetpasswordform

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('category/<slug:val>',views.CategoryView.as_view(),name='category'),
    path('product_details/<int:pk>',views.ProductDetail.as_view(),name='product_details'),
    path('category-title/<val>',views.CategoryTitle.as_view(),name="category-title"),
    path('profile/',views.profile_view.as_view(),name='profile'),
    path('address/',views.address,name='address'),
    path('updateaddress/<int:pk>',views.updateaddress.as_view(),name='updateaddress'),


    #### CART 
    path('add_to_cart/',views.add_to_cart,name='add_to_cart'),
    path('cart/',views.show_cart,name='cart'),
    path('checkout/',views.add_to_cart,name='checkout'),
    path('pluscart/',views.plus_cart,name='pluscart'),






    # Login authentication
    path('login/',views.Loginview.as_view(),name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'),
    path('registration/',views.CustomerRegistrationView.as_view(), name='customerregistration'),
    
    path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html',form_class=myPasswordChangeForm,success_url='/passwordchangedone'),name='passwordchange'),
    path('passwordchangedone/',auth_views.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'),name='passwordchangedone'),
    
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='app/password_reset.html',form_class=mypasswordresetform),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'),name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html',form_class=mysetpasswordform),name='password_reset_confirm'),
    path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'),name='password_reset_complete')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

