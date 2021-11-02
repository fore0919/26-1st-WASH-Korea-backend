from django.db import models

# Create your models here.

class Category(models.Model):
    name              = models.CharField(max_length=40)

    class Meta:
        db_table = 'categories'

class SubCategory(models.Model):
    name         = models.CharField(max_length=40)
    category     = models.ForeignKey('Category',on_delete=models.CASCADE)

    class Meta:
        db_table = 'sub_categories'

class Product(models.Model):
    name         = models.CharField(max_length=40)
    price        = models.DecimalField(max_digits=8, decimal_places=2)
    weight       = models.CharField(max_length=10)
    sub_name     = models.CharField(max_length=40)
    descriptio   = models.TextField()
    sub_category = models.ForeignKey('SubCategory',on_delete=models.CASCADE)
    tag          = models.ManyToManyField('Tag', through='ProductTag')
    
    class Meta:
        db_table = 'products'

class Tag(models.Model):
    name         = models.CharField(max_length=40)
    
    class Meta:
        db_table = 'tags'

class ProductTag(models.Model):
    product      = models.ForeignKey('Product', on_delete=models.CASCADE)
    tag          = models.ForeignKey('Tag', on_delete=models.CASCADE)
   
    class Meta:
        db_table = 'product_tags'

class Image(models.Model):
    url         = models.CharField(max_length=200)
    product      = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'imege'
