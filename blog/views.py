from datetime import datetime

from django.core.mail import send_mail, BadHeaderError
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views import View

from menu.models import MenuItem
from pages.models import Pages
from .forms import ContactForm
from .models import Category, Post


class PostListView(View):
    """Вывод категории и вывод стати"""

    # запрос к базе по полю публикации на true и по дате на сегодня которые должны выводится
    def get_queryset(self):
        return Post.objects.filter(published=True)

    def get(self, request, category_slug=None, tag_slug=None):
        form = ContactForm()
        if category_slug is not None:
            posts = self.get_queryset().filter(category__slug=category_slug, category__published=True)
        elif tag_slug is not None:
            posts = self.get_queryset().filter(tags__slug=tag_slug, tags__published=True)
        else:
            posts = self.get_queryset()
        paginator = Paginator(posts, 4)
        page = self.request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            posts = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            posts = paginator.page(paginator.num_pages)

        context = {
            'post_list': posts,
            'form':form,
        }

        return render(request, 'blog/home.html', context)



class PostDetailView(View):
    """Полная статья одного статьи"""

    def get(self, request, **kwargs):

        post = get_object_or_404(Post, slug=kwargs.get("slug"))
        photoitems = post.photoitems.all()
        form = ContactForm()
        context = {
            'post': post,
            'form': form,
            'photoitems': photoitems
        }
        return render(request, 'blog/detail.html', context)

    def post(self, request, **kwargs):

        post = get_object_or_404(Post, slug=kwargs.get("slug"))
        contact = Pages.objects.get(id=1)
        sent = False
        if request.method == 'POST':
            form = ContactForm(request.POST)
        # Если форма заполнена корректно, сохраняем все введённые пользователем значения
        if form.is_valid():
            cd = form.cleaned_data
            subject = 'Новый запрос от {} по почте {}'.format(cd['name'], cd['email'])
            sender = cd['email']
            phone = cd['phone']
            message = 'Имя клиента: {} \nТелефон клиента: {} \nПочта клиента: {}\nТекст запроса: {}\n{} Со страницы'.format(
                cd['name'], cd['phone'], cd['email'], cd['message'], post)

            recipients = ['zakaz@mnka.kz']
            # Если пользователь захотел получить копию себе, добавляем его в список получателей
            # if copy:
            #     recipients.append(sender)
            try:
                send_mail(subject, message, 'zakaz@mnka.kz', recipients)
                sent = True
            except BadHeaderError:  # Защита от уязвимости
                return HttpResponse('Invalid header found')
            # Переходим на другую страницу, если сообщение отправлено
            context = {
                'contact': contact,
                'form': form,
                'sent': sent, }
            return render(request, 'blog/detail.html', context)
        else:
            # Заполняем форму
            form = ContactForm()
        return render(request, 'blog/detail.html', context)


class ContactDetailView(View):
    """Полная статья одного статьи"""

    def get(self, request, **kwargs):

        contact = Pages.objects.get(id=1)
        form = ContactForm()

        context = {
            'contact': contact,
            'form': form,

        }
        return render(request, 'blog/page.html', context)

    def post(self, request, **kwargs):

        contact = Pages.objects.get(id=1)

        sent = False
        if request.method == 'POST':
            form = ContactForm(request.POST)
        # Если форма заполнена корректно, сохраняем все введённые пользователем значения
        if form.is_valid():
            cd = form.cleaned_data
            subject = 'Новый запрос от {} по почте {}'.format(cd['name'], cd['email'])
            sender = cd['email']
            phone = cd['phone']
            message = 'Имя клиента: {} \nТелефон клиента: {} \nПочта клиента: {}\nТекст запроса: {}\n Чувак хочеть 20% скидку'.format(cd['name'],
                                                                                                            cd['phone'],
                                                                                                            cd['email'],
                                                                                                            cd[
                                                                                                                'message'])

            recipients = ['zakaz@mnka.kz']
            # Если пользователь захотел получить копию себе, добавляем его в список получателей
            # if copy:
            #     recipients.append(sender)
            try:
                send_mail(subject, message, 'zakaz@mnka.kz', recipients)
                sent = True
            except BadHeaderError:  # Защита от уязвимости
                return HttpResponse('Invalid header found')
            # Переходим на другую страницу, если сообщение отправлено
            context = {


                'contact': contact,
                'form': form,
                'sent': sent, }
            return render(request, 'blog/page.html', context)
        else:
            # Заполняем форму
            form = ContactForm()
        return render(request, 'blog/page.html', context)


class FagDetailView(View):
    """Полная статья одного статьи"""

    def get(self, request, **kwargs):
        form = ContactForm()
        fag = Pages.objects.get(id=2)
        context = {

            'fag': fag,
            'form': form,

        }
        return render(request, 'blog/page.html', context)
