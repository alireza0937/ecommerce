from django.db import models
from django.utils.text import slugify
from category.models import Category


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    images = models.ImageField(upload_to='photos/product')
    slug = models.SlugField(unique=True, editable=False, db_index=True, max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_available = models.BooleanField(default=True)
    stock = models.IntegerField()
    
    
    class Meta:
        verbose_name_plural = 'Products'
        db_table = 'Products'
        
        
    def __str__(self):
        return self.name
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)