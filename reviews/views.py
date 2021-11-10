import json
from django.core.exceptions import MultipleObjectsReturned

from django.http  import JsonResponse
from json.decoder import JSONDecodeError
from django.views import View

from core.utils      import login_decorator
from reviews.models  import Review
from products.models import Product

class ReviewListView(View): #product id를 통해서 해당 제품의 전체 리뷰를 가져오는 api로 바뀌어야 한다.
    def get(self, request):
        product_id = request.GET['product_id']
        reviews    = Review.objects.filter(product_id = product_id)
        result     = []
        
        for review in reviews:
            data = {
                'review_id'    : review.id,
                'user_id'      : review.user.id,
                'user_name'    : review.user.user_name,
                'product_id'   : review.product.id,
                'product_name' : review.product.name,
                'rating'       : review.rating,
                'content'      : review.content,
                'image'        : review.image,
                'created_at'   : review.created_at,
                'updated_at'   : review.updated_at,
            }
            result.append(data)
        return JsonResponse({'message':result}, status =200)

class ReviewView(View):
    @login_decorator 
    def post(self, request):
        try:
            data       = json.loads(request.body)
            product_id = data['product_id']
            content    = data['content']
            image      = data['image']
            rating     = data['rating']

            if not Product.objects.filter(id = product_id).exists():
                return JsonResponse({'message' : 'DOES_NOT_EXISTS'}, status=404)    

            Review.objects.create(
                user_id    = request.user.id, 
                product_id = product_id,
                content    = content, 
                image      = image,
                rating     = rating
            )           
            return JsonResponse({'message' : 'SUCCESS'}, status=201)
       
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)

        except JSONDecodeError:
            return JsonResponse({'message':'JSON_DECODE_ERROR'}, status = 400)

    @login_decorator
    def patch(self, request, review_id):
        try:
            data = json.loads(request.body)
            user = request.user

            if not Review.objects.filter(id=review_id, user_id=user).exists():
                return JsonResponse({'message' : 'DOES_NOT_EXISTS'}, status=404)

            review = Review.objects.get(id=review_id, user_id=user)
         
            review.image   = data['image']
            review.rating  = data['rating']
            review.content = data['content']
            review.save()
 
            return JsonResponse({'message' : 'SUCCESS'}, status=201)

        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)

        except JSONDecodeError:
            return JsonResponse({'message':'JSON_DECODE_ERROR'}, status = 400)

    @login_decorator
    def delete(self, request, review_id):
        if not Review.objects.filter(id=review_id).exists():
            return JsonResponse({'message' : 'DOES_NOT_EXISTS'}, status=404)

        user   = request.user
        review = Review.objects.get(id=review_id, user_id=user)
        review.delete()

        return JsonResponse({'message' : 'SUCCESS'}, status = 204)

    def get(self, request, review_id):
        #처음 만들었던 review get method
        pass