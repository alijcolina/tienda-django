from django.contrib import admin
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name', 'slug', 'description', 'cat_image')
    search_fields = ('category_name',)
    list_filter = ('category_name',)
    list_editable = ('description', 'cat_image')
    list_per_page = 10
    ordering = ('category_name',)
    list_display_links = ('category_name',)

        
admin.site.register(Category, CategoryAdmin)

