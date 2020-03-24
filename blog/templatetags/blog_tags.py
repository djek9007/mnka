from django import template

from menu.models import MenuItem
from ..models import Category

register = template.Library()


@register.inclusion_tag('tags/blog/category_tags.html')
def show_category():
    categories = Category.objects.filter(published=True)
    return {'categories': categories}


@register.inclusion_tag('tags/blog/menu_tags.html')
def show_menu():
    menu = MenuItem.objects.filter(published=True)
    return {'menu': menu}
