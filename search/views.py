from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

# Create your views here.
from django.views import View

from blog.forms import ContactForm
from blog.models import Post, Category
from menu.models import MenuItem


def render_to_response(template_name, context):
    pass


class ESearchView(View):
    template_name = 'search/index.html'

    def get(self, request, *args, **kwargs):
        context={}
        context['form'] = ContactForm()

        question = request.GET.get('q')

        if question is not None:

            search_articles = Post.objects.filter(title__istartswith=question) | Post.objects.filter(text__icontains=question)

            # формируем строку URL, которая будет содержать последний запрос
            # Это важно для корректной работы пагинации
            context['last_question'] = '?q=%s' % question

            current_page = Paginator(search_articles, 5)

            page = request.GET.get('page')
            try:
                context['post_list'] = current_page.page(page)
            except PageNotAnInteger:
                context['post_list'] = current_page.page(1)
            except EmptyPage:
                context['post_list'] = current_page.page(current_page.num_pages)

        return render(request, template_name=self.template_name, context=context)
