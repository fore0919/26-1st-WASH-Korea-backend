import json

from django.http      import JsonResponse
from django.views     import View
from django.db.models import Q

from products.models import Product, SubCategory, Category

class ProductListView(View):
    def get(self, request):
        try:
            category     = request.GET['category']
            sub_category = request.GET.get('sub_category')
            sorting      = request.GET.get('sort', 'id')

            q = Q()

            if category:
                q &= Q(sub_category__category_id= category)
                products_header = Category.objects.get(id=category)

            if sub_category:
                q &= Q(sub_category_id = sub_category)
                products_header = SubCategory.objects.get(id=sub_category)

            sort = {
                "price"  : "price",
                "-price" : "-price",
                "id"     : "id"
            }

            results = {
                "data" : [{
                    "id"            : product.id,
                    "name"          : product.name,
                    "price"         : int(product.price),
                    "sub_name"      : product.sub_name,
                    'tags'          : [tag.name for tag in product.tags.all()],
                    "product_image" : [image.url for image in product.images.all()]    
                } for product in Product.objects.filter(q).order_by(sort[sorting])],
                "products_header" : {
                    "name"        : products_header.name,
                    "image"       : products_header.image,
                    "description" : products_header.description
                }
            }

            return JsonResponse({'results' : results}, status = 200)
        
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)

class CategoryListView(View):
    def get(self, request):
        result = [{
            "category_id"    : category.id,
            "category_name"  : category.name,
            "sub_categories" : [{
                "sub_category_id"   : sub_category.id,
                "sub_category_name" : sub_category.name
            }for sub_category in category.subcategory_set.all()]
        }for category in Category.objects.all()]

        return JsonResponse({'results' : result}, status = 200)

class CategoryView(View):
    def get(self, request, category_id):
        try:
            if not Category.objects.filter(id=category_id).exists():
                return JsonResponse({'message' : 'DOES NOT EXISTS'}, status=404)

            category = Category.objects.get(id=category_id)

            result = {
                "category_id"   : category.id,
                "category"      : category.name,
                "count"         : Product.objects.filter(sub_category_id__category_id=category).count(),
                "subcategories" : [{
                    "sub_category_id" : sub_category.id,
                    "name" : sub_category.name,
                    "count" : sub_category.product_set.count()
                }for sub_category in category.subcategory_set.all()]
            }
            return JsonResponse({'results' : result}, status = 200)
        
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)

class SearchView(View):
    def get(self, request):
        search_word = request.GET.get('search_word')
        sorting     = request.GET.get('sort', 'id')

        q = Q()
        
        if search_word:
            q = Q(sub_category__category__name__contains = search_word)|\
                Q(sub_category__name__contains = search_word)|\
                Q(name__contains = search_word)|\
                Q(tags__name__contains = search_word)

        sort = {
                "price"  : "price",
                "-price" : "-price",
                "id"     : "id"
            }

        results = {
            "data" : [{
                "id"            : product.id,
                "name"          : product.name,
                "price"         : int(product.price),
                "sub_name"      : product.sub_name,
                'tags'          : [tag.name for tag in product.tags.all()],
                "product_image" : [image.url for image in product.images.all()]
            } for product in Product.objects.filter(q).distinct().order_by(sort[sorting])],
            "search_hedaline"   : {
                "word"  : search_word,
                "count" : Product.objects.filter(q).distinct().order_by(sort[sorting]).count()
            }
        }
        return JsonResponse({'results' : results}, status = 200)

class ProductDetailView(View):
    def get(self, request, product_id):
        try:
            if not Product.objects.filter(id=product_id).exists():
                return JsonResponse({'message' : 'DOES NOT EXISTS'}, status=404) 
            
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