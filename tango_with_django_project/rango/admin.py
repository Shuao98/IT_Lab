from django.contrib import admin

# Register your models here.
from rango.models import Category, Page


# admin.site.register(Category)
admin.site.register(Page)

class PageAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'url')
# Add in this class to customise the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
# Update the registration to include this customised interface
admin.site.register(Category, CategoryAdmin)