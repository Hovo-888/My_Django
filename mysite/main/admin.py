from django.contrib import admin
from .models import Category,Product, Cart, Contact

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','price']
    list_display_links = ['id', 'name']
    search_fields = ['name']

admin.site.register(Cart)  

admin.site.register(Contact)

# Register your models here.
