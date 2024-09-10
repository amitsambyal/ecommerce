from django.contrib import admin
from .models import Category,Subcategory,Product

class CategoryAdmin(admin.ModelAdmin):
    list_display=["name"]

@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display=["name","category"]
      

# Register your models here.
admin.site.register(Category,CategoryAdmin)

@admin.register(Product)
class productAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'sub_category', 'price', 'date', 'featured','desc')
    search_fields = ('name', 'category__name', 'sub_category__name')   
    
    
    
#admin.site.register(Subcategory)
