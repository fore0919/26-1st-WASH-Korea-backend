from django.db import models

class User(models.Model):
    user_id	     = models.CharField(max_length=40)
    password     = models.CharField(max_length=200)
    name    	 = models.CharField(max_length=40)
    nickname     = models.CharField(max_length=40,null=True)
    email     	 = models.CharField(max_length=100, unique=True)
    contact      = models.CharField(max_length=15)
    address	     = models.CharField(max_length=100,null=True)
    created_at 	 = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'
