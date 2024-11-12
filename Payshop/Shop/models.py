from builtins import super

from django.db import models
from django.conf import settings

# Create your models here.
class Sections(models.Model):
    section_name=models.CharField(max_length=201)
    sect_img=models.ImageField(upload_to='media/sections/',blank=True)
    def __str__(self):
        return self.section_name
class Category(models.Model):
    catgory = models.CharField(max_length=200, default='', null=False, blank=True)
class Size(models.Model):
    value = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.value

class product(models.Model):
    pr_name=models.CharField(max_length=46,default='')
    supereller = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, default=1,
                               on_delete=models.SET_NULL)
    price = models.IntegerField(default=0)
    image=models.FileField(upload_to='product/',default='')

    barcode_image=models.ImageField(upload_to='kak',blank=True,null=True)
    section=models.ForeignKey(Sections,null=True,on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    size = models.ManyToManyField(Size, blank=True)
    slug_name = models.SlugField(default='', blank=True)
    stock = models.IntegerField(default=0)
    description = models.TextField(max_length=200, default='')
    code = models.CharField(default='', null=True, blank=True, max_length=9)
    barcode_img = models.ImageField(upload_to="image/", blank=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)