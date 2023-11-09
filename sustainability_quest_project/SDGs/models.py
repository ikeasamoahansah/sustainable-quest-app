from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Image(models.Model):
#     image = models.ImageField(upload_to='posts/', null=True, blank=True)
   
    # def __str__(self):
    #     return self.title


class Goal(models.Model):
    name = models.CharField(max_length=200, null=True)
    title = models.CharField(max_length=200)
    content1 = models.TextField()
    content2 = models.TextField(null=True)
    photo = models.ImageField(upload_to='posts/', null=True, blank=True)
    # images = models.ManyToManyField(Image)
    image1 = models.ImageField(upload_to='posts/', null=True, blank=True)
    image2 = models.ImageField(upload_to='posts/', null=True, blank=True)
    image3 = models.ImageField(upload_to='posts/', null=True, blank=True)


    def __str__(self):
        return self.title

