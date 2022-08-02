from django.contrib import admin
from django import forms
from mptt.admin import DraggableMPTTAdmin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import *

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = ProductList
        fields = '__all__'


class CategoryAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',)
    list_display_links = ('indented_title',)
    prepopulated_fields = {"slug": ("title",)}


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    save_as = True
    list_display = ('title', 'category', 'price', 'published')
    list_display_links = ('title',)
    search_fields = ('title',)
    list_filter = ('category',)







admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductList, ProductAdmin)