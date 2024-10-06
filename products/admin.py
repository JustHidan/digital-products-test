from django.contrib import admin
from products.models import Product,File,Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [ 'title','parent' ,'created_time']
    list_filter = ['parent']
    search_fields = ['title']

class FileInlineAdmin (admin.StackedInline):
    model = File
    fields = ['title','file','is_enabled']
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','created_time']
    list_filter = ['created_time']
    search_fields = ['title']
    filter_horizontal = ['categories']
    inlines = [FileInlineAdmin]

# Register your models here.
