from django.urls import path
from django.views.generic import TemplateView
from .views import ProductHomeView, ProductListView, ProductDetailView

app_name = 'products'


urlpatterns = [
    
    path('', ProductHomeView.as_view(), name='home'),
    path('category/<int:id>/', ProductListView.as_view(), name='category_products'),
    path('<int:id>/detail/', ProductDetailView.as_view(), name='product_detail'),
    
    
]