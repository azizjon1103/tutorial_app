from django.contrib import admin
from .models import Category, Product
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug' : ('name',) }

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['category','author','title', 'slug','create','update', 'is_activated']
    list_filter = ['category', 'author', 'is_activated']
    list_editable = ['is_activated']
    prepopulated_fields = {'slug': ('title',)}