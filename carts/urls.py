from django.urls import path
from carts.views import CartView, CartListView

urlpatterns = [
    path('',CartListView.as_view()),
    path('/<int:cart_id>',CartView.as_view())
]