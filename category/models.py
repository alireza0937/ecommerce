from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='photos/category')
    slug = models.SlugField(unique=True, editable=False, db_index=True, max_length=200)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
    
    
    class Meta:
        verbose_name_plural = 'Categories'
        db_table = 'Categories'