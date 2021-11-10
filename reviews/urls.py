from django.urls import path
from reviews.views import ReviewListView, ReviewView

urlpatterns = [
      path('',ReviewListView.as_view()),
    path('',ReviewView.as_view()),
    path('/<int:review_id>',ReviewView.as_view())
]
