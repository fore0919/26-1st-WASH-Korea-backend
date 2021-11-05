from django.urls import path

from products.views import ProductListView

urlpatterns = [
    path('/products', ProductListView.as_view()),
    path('/products/<int:sub_category>', ProductListView.as_view())
]
