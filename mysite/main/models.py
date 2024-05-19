from django.db import models

class Category(models.Model):

    name = models.CharField('Category name', max_length=60)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
# Create your models here.

class Product(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cat_prod')
    name = models.CharField('Product name', max_length=60)
    price = models.PositiveIntegerField('Product price')
    img = models.ImageField('product image', upload_to='home_imaes')
    about = models.TextField('Product about')
    slug = models.SlugField('Product slug', unique=True)

    def __str__(self):
        return self.name
    
class Cart(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)    
    
class Contact(models.Model):

    email = models.EmailField('Contact email')
    subject = models.CharField('Contact subject', max_length=50)
    message = models.TextField('Contact message')

    def __str__(self):
        return self.email
    