import json

from django.http      import JsonResponse
from django.views     import View
from django.db.models import Q

from products.models import Product, SubCategory

class ProductListView(View):
    def get(self, request):
        category     = request.GET['category']
        sub_category = request.GET.get('sub_category')
        price        = request.GET.get('price')

        q = Q()

        if category:
            q &= Q(sub_category__category_id= category)

        if sub_category:
            q &= Q(sub_category_id = sub_category)

        product_list = Product.objects.filter(q)

        if price:
            product_list = product_list.order_by(price)

        results = [{
                    "name"          : product.name,
                    "price"         : int(product.price),
                    "sub_name"      : product.sub_name,
                    'tags'          : [tag.name for tag in product.tags.all()],
                    "product_image" : [image.url for image in product.productimage_set.all()]
            } for product in product_list]

        return JsonResponse({'results' : results}, status = 200)

class NavListView(View):
    def get(self, request):
        category     = request.GET.get('category')
        sub_category = request.GET.get('sub_category')

        q = Q()

        if category:
            q &= Q(category_id = category)

        if sub_category:
            q &= Q(id = sub_category)

        sub_category_list = SubCategory.objects.filter(q)

        results = [{
                    "sub_category"             : sub_category.name,
                    "sub_category_image"       : sub_category.image,
                    "sub_category_description" : sub_category.description,
                    "category"                 : sub_category.category.name,
                    "category_image"           : sub_category.category.image,
                    "category_description"     : sub_category.category.description,
                    "account"                  : len(Product.objects.filter(sub_category_id = sub_category))
            } for sub_category in sub_category_list]

        return JsonResponse({'results' : results}, status = 200)

class SearchView(View):
    def get(self, request):
        search_word = request.GET.get('search_word')

        q = Q()

        if search_word:
            q = Product.objects.filter(Q(sub_category__category__name__startswith = search_word)|Q(sub_category__name__startswith = search_word)|Q(name__startswith = search_word)|Q(tags__name__startswith = search_word))

        results = [{
                    "name"          : product.name,
                    "price"         : int(product.price),
                    "sub_name"      : product.sub_name,
                    'tags'          : [tag.name for tag in product.tags.all()],
                    "product_image" : [image.url for image in product.productimage_set.all()]
            } for product in q]

        return JsonResponse({'results' : results}, status = 200)