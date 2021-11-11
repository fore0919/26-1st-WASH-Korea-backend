from django.urls import path, include

from products.views import CategoryView, CategoryListView

urlpatterns = [
    path("users", include("users.urls")),
    path("products", include("products.urls")),
    path("reviews", include("reviews.urls")),
    path("categories", CategoryListView.as_view()),
    path("categories/<int:category_id>", CategoryView.as_view()),
]