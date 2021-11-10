from django.urls import path
from reviews.views import ReviewView, ReviewListView

urlpatterns = [
    path('',ReviewListView.as_view()),
    path('',ReviewView.as_view()),
    path('/<int:review_id>',ReviewView.as_view())
]
#/reviews
#/reviews/<review_id>