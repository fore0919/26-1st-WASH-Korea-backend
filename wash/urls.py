from django.urls import path, include

from products.views import Productcategory, CategoryListView

urlpatterns = [
    path("users", include("users.urls")),
    path("products", include("products.urls")),
    path("categories", CategoryListView.as_view()),
    path("categories/<int:category_id>", Productcategory.as_view())
]