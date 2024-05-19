
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('category/<slug:val>',views.CategoryView.as_view(),name='category'),
    path('product_details/<int:pk>',views.ProductDetail.as_view(),name='product_details')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

