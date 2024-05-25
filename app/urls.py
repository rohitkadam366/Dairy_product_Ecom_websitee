
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('category/<slug:val>',views.CategoryView.as_view(),name='category'),
    path('product_details/<int:pk>',views.ProductDetail.as_view(),name='product_details'),
    path('category-title/<val>',views.CategoryTitle.as_view(),name="category-title"),


    # Login authentication
    path('login/',views.Loginform.as_view(),name='login'),
    # path('logout/',views.logout,name='logout'),
    path('registration/',views.CustomerRegistrationView.as_view(), name='customerregistration'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

