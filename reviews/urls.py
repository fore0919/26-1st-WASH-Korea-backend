from django.urls import path
from reviews.views import ReviewDeleteView, ReviewUpdateView, ReviewView, PostingView

urlpatterns = [
    path('/<int:product_id>/<int:review_id>',ReviewView.as_view()),
    path('/post/<int:product_id>',PostingView.as_view()),
    path('/delete/<int:review_id>',ReviewDeleteView.as_view()),
    path('/update/<int:review_id>',ReviewUpdateView.as_view()),
] 