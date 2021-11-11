import json

from json.decoder import JSONDecodeError

from django.http      import JsonResponse
from django.views     import View

from carts.models import Cart
from core.utils   import login_decorator


class CartListView(View):
    @login_decorator
    def get(self, request):
        user = request.GET['user']

        result = [{
            "cart_id"         : cart.id,
            "user_id"         : cart.user.id,
            "product_id"      : cart.product.id,
            "product_name"    : cart.product.name,
            "product_price"   : int(cart.product.price),
            "product_image"   : cart.product.images.all()[0].url,
            "sub_category_id" : cart.product.sub_category_id,
            "quantity"        : cart.quantity
        } for cart in Cart.objects.filter(user_id =user)]

        return JsonResponse({'results' : result}, status = 200)

    @login_decorator
    def post(self, request):
        try:
            data = json.loads(request.body)
            product_id = data['product_id']
            quantity   = data['quantity']

            cart, created = Cart.objects.get_or_create(
                user_id    = request.user.id, 
                product_id = product_id,
                defaults={'quantity': quantity}
            )
            if not created:
                cart.quantity += quantity
                cart.save()

            return JsonResponse({'message' : 'SUCCESS'}, status=201)
       
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)

        except JSONDecodeError:
            return JsonResponse({'message':'JSON_DECODE_ERROR'}, status = 400)

class CartView(View):
    @login_decorator
    def patch(self, request, cart_id):
        try:
            data = json.loads(request.body)
            user = request.user

            if not Cart.objects.filter(id=cart_id, user_id=user).exists():
                return JsonResponse({'message' : 'DOES_NOT_EXISTS'}, status=404)

            cart = Cart.objects.get(id=cart_id, user_id=user.id)

            cart.product_id = data['product_id']
            cart.quantity   = data['quantity']
            cart.save()

            return JsonResponse({'message' : 'SUCCESS'}, status=201)
       
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)

        except JSONDecodeError:
            return JsonResponse({'message':'JSON_DECODE_ERROR'}, status = 400)

    @login_decorator
    def delete(self, request, cart_id):
        user   = request.user
        review = Cart.objects.get(id=cart_id, user_id=user)

        if not Cart.objects.filter(id=cart_id, user_id=user).exists():
            return JsonResponse({'message' : 'DOES_NOT_EXISTS'}, status=404)

        review.delete()

        return JsonResponse({'message' : 'SUCCESS'}, status = 204)