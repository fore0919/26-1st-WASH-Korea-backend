import json

from django.http      import JsonResponse
from django.views     import View
from django.db.models import Q

from products.models import Product, SubCategory

class ProductListView(View):
    def get(self, request):
        DEFAULT_CATEGORY_ID = 1
    
        data         = json.loads(request.body)
        category     = data.get('category', DEFAULT_CATEGORY_ID)
        sub_category = data.get('sub_category')
        sorting      = data.get('sort', 'id')

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
                    "name"          : product.name,
                    "price"         : int(product.price),
                    "sub_name"      : product.sub_name,
                    'tags'          : [tag.name for tag in product.tags.all()],
                    "product_image" : [image.url for image in product.productimage_set.all()]
            } for product in Product.objects.filter(q).order_by(sort[sorting])]

        return JsonResponse({'results' : results}, status = 200)

class CategoryView(View):
    def get(self, request):
        category     = request.GET.get('category')
        sub_category = request.GET.get('sub_category')

        q = Q()

        if category:
            q &= Q(category_id = category)

        if sub_category:
            q &= Q(id = sub_category)

        sub_category = SubCategory.objects.filter(q)
        results = {
                    "category"
                    "sub_category"             : sub_category.name,
                    "sub_category_image"       : sub_category.image,
                    "sub_category_description" : sub_category.description,
                    "category"                 : sub_category.category.name,
                    "category_image"           : sub_category.category.image,
                    "category_description"     : sub_category.category.description,
                    "account"                  : len(Product.objects.filter(sub_category_id = sub_category))
            }

        return JsonResponse({'results' : results}, status = 200)

class SearchView(View):
    def get(self, request):
        search_word = request.GET.get('search_word')

        if search_word:
            products = Product.objects.filter(
                Q(sub_category__category__name__startswith = search_word)|
                Q(sub_category__name__startswith = search_word)|
                Q(name__startswith = search_word)|
                Q(tags__name__startswith = search_word)
            )

        results = [{
                    "name"          : product.name,
                    "price"         : int(product.price),
                    "sub_name"      : product.sub_name,
                    'tags'          : [tag.name for tag in product.tags.all()],
                    "product_image" : [image.url for image in product.productimage_set.all()]
            } for product in products]

        return JsonResponse({'results' : results}, status = 200)