from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from . forms import mypasswordresetform

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('category/<slug:val>',views.CategoryView.as_view(),name='category'),
    path('product_details/<int:pk>',views.ProductDetail.as_view(),name='product_details'),
    path('category-title/<val>',views.CategoryTitle.as_view(),name="category-title"),
    path('profile/',views.profile_view.as_view(),name='profile'),
    path('address/',views.address,name='address'),

    # Login authentication
    path('login/',views.Loginview.as_view(),name='login'),
    # path('logout/',views.logout,name='logout'),
    path('registration/',views.CustomerRegistrationView.as_view(), name='customerregistration'),
    # path('password_reset/',auth_views.PasswordResetView.as_view(template_name='app/password_reset.html',form_class=mypasswordresetform),name='password_reset'),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

