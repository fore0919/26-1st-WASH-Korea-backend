from django.urls import path, include

urlpatterns = [
    path('main', include('products.urls')),
]