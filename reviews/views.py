import json

from django.http    import JsonResponse
from django.views   import View

from core.utils      import login_decorator
from reviews.models  import Review
from products.models import Product

class ReviewsView(View):
    def get(self, request):
        result = [
            {
                'user_id' : reviews.user_id,

            }
        ]
