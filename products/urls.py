from django.urls import path
from products.views import ProductDetailView

urlpatterns = [
    path('products/<int:id>', ProductDetailView.as_view()),  
] 
