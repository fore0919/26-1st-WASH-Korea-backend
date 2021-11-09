from django.urls import path
from products.models import Category

from products.views import ProductListView, CategoryListView, SubcategoryListView, SearchView

urlpatterns = [
    path('/productlist', ProductListView.as_view()),
    path('/categorylist', CategoryListView.as_view()),
    path('/subcategorylist', SubcategoryListView.as_view()),
    path('/search', SearchView.as_view()),
]
