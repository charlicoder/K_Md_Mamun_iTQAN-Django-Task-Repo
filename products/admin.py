from django.contrib import admin
from .models import Category, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'current_hit_count')
    
    # def formatted_hit_count(self, obj):
    #     return obj.current_hit_count
    
    # formatted_hit_count.admin_order_field = 'hit_count'
    # formatted_hit_count.short_description = 'Hits'


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
# Register your models here.
