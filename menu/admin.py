from django.contrib import admin

# Register your models here.
from .models import Menu,MenuItem
from mptt.admin import MPTTModelAdmin

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    """Меню"""
    list_display = ("name", "status", "published")
    list_filter = ("published",)
    #actions = ['unpublish', 'publish']


@admin.register(MenuItem)
class MenuItemAdmin(MPTTModelAdmin):
    """Пункты меню"""
    #form = MenuItemAdminForm
    list_display = ("title", "parent", "menu", "sort", "published")
    list_filter = ("menu", "parent", "published")
    search_fields = ("title", "parent__title", )
    save_as = True
    list_editable = ("sort", "published")
    mptt_level_indent = 20

    #actions = ['unpublish', 'publish']
    save_on_top = True