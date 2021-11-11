from django.urls import path

from products.views import ProductDetailView, ProductListView, SearchView

urlpatterns = [
    path('/productlist', ProductListView.as_view()),
    path('/search', SearchView.as_view()),
    path('/<int:product_id>', ProductDetailView.as_view()), 
]