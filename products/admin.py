from django.contrib import admin
from .models import Category, Product


class ProductAdmin(admin.ModelAdmin):
	list_display = ('name', 'category', 'image', 'view_count')


admin.site.register(Category, ProductAdmin)
admin.site.register(Product)
# Register your models here.
