from datetime import datetime

from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views import View

from menu.models import MenuItem
from pages.models import Pages
from .models import Category, Post


class PostListView(View):
    """Вывод категории и вывод стати"""


    # запрос к базе по полю публикации на true и по дате на сегодня которые должны выводится
    def get_queryset(self):
        return Post.objects.filter(published=True, published_date__lte=datetime.now())

    def get(self, request, category_slug=None, tag_slug=None):
        categories = Category.objects.filter(published=True)
        menu = MenuItem.objects.filter(published=True)

        if category_slug is not None:
            posts = self.get_queryset().filter(category__slug=category_slug, category__published=True)
        elif tag_slug is not None:
            posts = self.get_queryset().filter(tags__slug=tag_slug, tags__published=True)
        else:
            posts = self.get_queryset()

        context = {
            'categories': categories,
            'post_list': posts,
            'menu': menu,
        }
        return render(request, 'blog/home.html', context)


class PostDetailView(View):
    """Полная статья одного статьи"""
    def get(self, request, **kwargs):
        # categories = Category.objects.filter(published=True)
        post = get_object_or_404(Post, slug=kwargs.get("slug"))
        menu = MenuItem.objects.filter(published=True)
        context = {
            'post': post,
            'menu': menu,
        }
        return render(request, 'blog/detail.html', context)


class ContactDetailView(View):
    """Полная статья одного статьи"""
    def get(self, request, **kwargs):
        contact = Pages.objects.get(id=1)
        # fag = Pages.objects.get(id=2)
        context = {
            # 'post': post,

            'contact': contact,
        }
        return render(request, 'blog/page.html', context)

class FagDetailView(View):
    """Полная статья одного статьи"""
    def get(self, request, **kwargs):
        # categories = Category.objects.filter(published=True)
        # contact = Pages.objects.get(id=1)
        fag = Pages.objects.get(id=2)
        context = {
            # 'post': post,
            # 'categories': categories,
            # 'contact': contact,
            'fag': fag,
        }
        return render(request, 'blog/page.html', context)