from django.db import models

# Create your models here.
class product(models.Model):
    fullname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    username=models.CharField(max_length=200)


# class post(models.Model):
#     pic = models.ImageField(upload_to='media/images' ,default='')
#     bio = models.CharField(max_length=200,default='' )

class posts(models.Model):
        pic = models.ImageField(upload_to='media/images', default='')
        bio = models.CharField(max_length=200, default='')

        class MyClass:
            def __init__(self):
                self.objects = []

