
import json

from django.http    import JsonResponse
from django.views   import View

from products.models   import Product

class ProductDetailView(View):
    def get(self, request, product_id):
        try:
            if not Product.objects.filter(id=product_id).exists():
                return JsonResponse({'message' : '상품 상세정보가 존재하지 않습니다.'}, status=404) 
            
            product = Product.objects.get(id=product_id)
            
            result = {
                'id'          : product.id,
                'name'        : product.name, 
                'price'       : int(product.price),
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
                'product_image' : [{
                    'id'  : product_image.id,
                    'url' : product_image.url,
                }for product_image in product.images.all()]}
            return JsonResponse({'result' : result}, status = 200)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400) 