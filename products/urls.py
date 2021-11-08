from django.urls import path
from products.models import Category

from products.views import ProductListView, CategoryListView, SubcategoryListView, SearchView

urlpatterns = [
    path('/productList', ProductListView.as_view()),
    path('/categoryList', CategoryListView.as_view()),
    path('/subcategoryList', SubcategoryListView.as_view()),
    path('/search', SearchView.as_view()),
]
