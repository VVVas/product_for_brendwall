from django.contrib import admin

from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description', 'price',)
    list_display_links = ('title',)
    search_fields = ('title', 'description',)
    empty_value_display = '-пусто-'


admin.site.register(Product, ProductAdmin)
