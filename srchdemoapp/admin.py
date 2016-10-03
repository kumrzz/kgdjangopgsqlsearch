from django.contrib import admin
from .models import Category, Listing

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name',]
admin.site.register(Category, CategoryAdmin)


class ListingAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price']
    list_filter = ['category',]
    list_editable = ['price',]
admin.site.register(Listing, ListingAdmin)
