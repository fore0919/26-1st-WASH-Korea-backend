
import json

from django.http    import JsonResponse
from django.views   import View

from products.models   import Product

class ProductDetailView(View):
    def get(self, request, id):
        try:
            product = Product.objects.get(id=id)
            product_info = [{
            'id'          : product.id,
            'name'        : product.name,
            'price'       : product.price,
            'weight'      : product.weight,
            'sub_name'    : product.sub_name,
            'description' : product.description,
            'category'    : {
                'id'   : product.sub_category.category.id,
                'name' : product.sub_category.category.name,
            },
            'sub_category' : { 
                'id'   : product.sub_category.id,
                'name' : product.sub_category.name,    
            },
            'product_image' : [
                {
                'id'  : product_image.id,
                'url' : product_image.url,
            }for product_image in product.productimage_set.all()]    
            }for product in Product.objects.filter(id=id)
            ]
            return JsonResponse({'result' : product_info}, status = 200)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400) 

        except Product.DoesNotExist:
            return JsonResponse({'message' : '상품 상세정보가 존재하지 않습니다.'}, status=404) 