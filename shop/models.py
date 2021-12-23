from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse 
# Create your models here.

class Category(models.Model):
    cat_name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(max_length=100,unique=True)

    class Meta:
        ordering=('cat_name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    def get_url(self):
        return reverse('pct_home',args=[self.slug])
    
    def __str__(self):
        return '{}'.format(self.cat_name)

class Product(models.Model):
    name = models.CharField(max_length=100,unique=True) 
    slug = models.SlugField(max_length=100,unique=True)
    image = models.ImageField(upload_to='images')
    desc = models.TextField()
    stock = models.IntegerField()
    avail = models.BooleanField()
    price = models.IntegerField()
    prodcat = models.ForeignKey(Category,on_delete=models.CASCADE)

    class Meta:
        ordering=('name',)
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def get_prod_url(self):
        return reverse('details',args=[self.prodcat.slug,self.slug])

    def __str__(self) :
        return '{}'.format(self.name)