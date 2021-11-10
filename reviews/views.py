import json
from django.core.exceptions import MultipleObjectsReturned

from django.http  import JsonResponse
from json.decoder import JSONDecodeError
from django.views import View

from core.utils      import login_decorator
from reviews.models  import Review
from products.models import Product

class ReviewView(View):
    def get(self, request, product_id, review_id):
    
        if not Review.objects.filter(product_id = product_id, id=review_id).exists():
            return JsonResponse({'message' : 'DOES_NOT_EXISTS'}, status=404)

        review = Review.objects.get(id = review_id)
        result = {
            'user'         : review.user.id,
            'user_name'    : review.user.user_name,
            'product_id'   : review.product.id,
            'product_name' : review.product.name,
            'rating'       : review.rating,
            'content'      : review.content,
            'image'        : review.image,
            'created_at'   : review.created_at,
            'updated_at'   : review.updated_at,
        }
        return JsonResponse({'message':result}, status =200)

class PostingView(View):
    @login_decorator
    def post(self, request, product_id): 
        try:
            if not Product.objects.filter(id = product_id).exists():
                return JsonResponse({'message' : 'DOES_NOT_EXISTS'}, status=404)    

            data    = json.loads(request.body)

            Review.objects.create(
                user_id    = request.user.id, 
                product_id = product_id,
                content    = data['content'], 
                image      = data['image'],
                rating     = data['rating'],
                created_at = Review.created_at,
                updated_at = Review.updated_at,
            )           
            return JsonResponse({'message' : 'SUCCESS'}, status=201)
       
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)

        except JSONDecodeError:
            return JsonResponse({'message':'JSON_DECODE_ERROR'}, status = 400)

class ReviewDeleteView(View):
    @login_decorator
    def delete(self, request, review_id):
        if not Review.objects.filter(id=review_id).exists():
            return JsonResponse({'message' : 'DOES_NOT_EXISTS'}, status=404)

        user = request.user
        review = Review.objects.get(id=review_id, user_id=user)
        review.delete()

        return JsonResponse({'message' : 'SUCCESS'}, status = 201)

class ReviewUpdateView(View):
    @login_decorator
    def post(self, request, review_id):
        try:
            data = json.loads(request.body)

            if not Review.objects.filter(id=review_id).exists():
                return JsonResponse({'message' : 'DOES_NOT_EXISTS'}, status=404)

            user    = request.user
            review  = Review.objects.filter(id=review_id, user_id=user)

            review.update(
                content = data['content'],
                image   = data['image'],
                rating  = data['rating'],
            )          
            # review.image      = data.get('image', review.image)
            # review.rating     = data.get('rating', review.rating)
            # review.content    = data.get('content', review.content)
            # updated_at = Review.updated_at,
            # review.save()
 
            return JsonResponse({'message' : 'SUCCESS'}, status=201)

        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)

        except JSONDecodeError:
            return JsonResponse({'message':'JSON_DECODE_ERROR'}, status = 400)
