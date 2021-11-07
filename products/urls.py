from django.urls import path
from products.models import Category

from products.views import ProductListView, NavListView, SearchView

urlpatterns = [
    path('/productList', ProductListView.as_view()),
    path('/navList', NavListView.as_view()),
    path('/search', SearchView.as_view()),
]
