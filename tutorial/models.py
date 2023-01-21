from django.db import models
from ckeditor.fields import RichTextField
from django.shortcuts import reverse
# Create your models here.



class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_activated=True)

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    object = models.Manager()


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tutorial:category_list', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey('Category',related_name='obyekt', on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=550)
    slug = models.SlugField(unique=True)
    discription = RichTextField()
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    is_activated = models.BooleanField(default=True)
    progucts =ProductManager()

    class Meta:
        ordering = ('-create',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tutorial:product_detail', args=[self.slug])
