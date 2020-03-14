from django.shortcuts import render

# Create your views here.
from django.conf import settings
from django.http import Http404, HttpResponsePermanentRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import Pages


class PageDetailView(View):
    """Полная статья одного статьи"""
    def get(self, request, **kwargs):

        page = get_object_or_404(Pages, slug=kwargs.get("slug"))

        context = {
            'page': page,

        }
        return render(request, 'blog/detail.html', context)