import json

from django.http      import JsonResponse
from django.views     import View
from django.db.models import Q

from products.models import Product, Category, SubCategory

class ProductListView(View):
    def get(self, request):
        try:
            category     = request.GET['category']
            sub_category = request.GET.get('sub_category')
            sorting      = request.GET.get('sort', 'id')

            q = Q()

            if category:
                q &= Q(sub_category__category_id= category)

            if sub_category:
                q &= Q(sub_category_id = sub_category)

            sort = {
                "price"  : "price",
                "-price" : "-price",
                "id"     : "id"
            }

            results = [{
                        "id"            : product.id,
                        "name"          : product.name,
                        "price"         : int(product.price),
                        "sub_name"      : product.sub_name,
                        'tags'          : [tag.name for tag in product.tags.all()],
                        "product_image" : [image.url for image in product.productimage_set.all()]
                } for product in Product.objects.filter(q).order_by(sort[sorting])]

            return JsonResponse({'results' : results}, status = 200)
        
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)

class CategoryListView(View):
    def get(self, request):
        try:
            category = request.GET['category']

            if not Category.objects.filter(id=category).exists():
                return JsonResponse({'message' : 'DOES NOT EXISTS'}, status=404)

            q = Q()

            if category:
                q &= Q(id = category)

            category = Category.objects.get(q)

            results = {
                        "category"             : category.name,
                        "category_image"       : category.image,
                        "category_description" : category.description,
                        "account"              : Product.objects.filter(sub_category_id__category_id=category).count()
                }
            return JsonResponse({'results' : results}, status = 200)
        
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)

class SubcategoryListView(View):
    def get(self, request):
        try:
            sub_category = request.GET['sub_category']

            if not SubCategory.objects.filter(id=sub_category).exists():
                return JsonResponse({'message' : 'DOES NOT EXISTS'}, status=404)

            q = Q()

            if sub_category:
                q &= Q(id = sub_category)

            sub_category = SubCategory.objects.get(q)

            results = {
                        "sub_category"             : sub_category.name,
                        "sub_category_image"       : sub_category.image,
                        "sub_category_description" : sub_category.description,
                        "account"                  : Product.objects.filter(sub_category_id = sub_category).count()
                }
            return JsonResponse({'results' : results}, status = 200)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)

class SearchView(View):
    def get(self, request):
        search_word = request.GET.get('search_word')

        q = Q()
        
        if search_word:
            q = Q(sub_category__category__name__startswith = search_word)|\
                Q(sub_category__name__startswith = search_word)|\
                Q(name__startswith = search_word)|\
                Q(tags__name__startswith = search_word)

        results = [{
                    "id"            : product.id,
                    "name"          : product.name,
                    "price"         : int(product.price),
                    "sub_name"      : product.sub_name,
                    'tags'          : [tag.name for tag in product.tags.all()],
                    "product_image" : [image.url for image in product.productimage_set.all()]
            } for product in Product.objects.filter(q)]

        return JsonResponse({'results' : results}, status = 200)