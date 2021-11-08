from django.db import models

class Category(models.Model):
    name        = models.CharField(max_length=40)
    image       = models.CharField(max_length=2000)
    description = models.CharField(max_length=100)

    class Meta:
        db_table = 'categories'

class SubCategory(models.Model):
    name        = models.CharField(max_length=40)
    image       = models.CharField(max_length=2000)
    description = models.CharField(max_length=100)
    category    = models.ForeignKey('Category',on_delete=models.PROTECT)

    class Meta:
        db_table = 'sub_categories'

class Product(models.Model):
    name         = models.CharField(max_length=40)
    price        = models.DecimalField(max_digits=8, decimal_places=2)
    weight       = models.CharField(max_length=10)
    sub_name     = models.CharField(max_length=40)
    description  = models.TextField()
    sub_category = models.ForeignKey('SubCategory',on_delete=models.CASCADE)
    tags         = models.ManyToManyField('Tag', through='ProductTag')
    
    class Meta:
        db_table = 'products'

class Tag(models.Model):
    name = models.CharField(max_length=40)
    
    class Meta:
        db_table = 'tags'

class ProductTag(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    tag     = models.ForeignKey('Tag', on_delete=models.CASCADE)
   
    class Meta:
        db_table = 'products_tags'

class ProductImage(models.Model):
    url     = models.CharField(max_length=2000)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name="images")

    class Meta:
        db_table = 'product_images'
