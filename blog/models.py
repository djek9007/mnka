from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


# Create your models here.
class Category(MPTTModel):
    """Модель категории"""
    name = models.CharField("Название категории", max_length=100)
    slug = models.SlugField("url", max_length=100, unique=True)
    parent = TreeForeignKey(
        'self',
        verbose_name="Родительская категория",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    published = models.BooleanField("отображать?", default=True)
    sort = models.PositiveIntegerField('порядок', default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    class MPTTMeta:
        order_insertion_by = ('sort',)

    def get_absolute_url(self):
        return reverse('blog:category', kwargs={'category_slug': self.slug})

    # def get_category_template(self):
    #     return self.category.template


class Post(models.Model):
    """Модель постов"""
    title = models.CharField("Заголовок", max_length=250)
    mini_text = models.TextField("Короткое описание")
    text = models.TextField("Полный текст")
    create_date = models.DateTimeField("дата создания", auto_now=True)
    slug = models.SlugField("url", max_length=100, unique=True)
    edit_date = models.DateTimeField(
        "дата редактирования",
        default=timezone.now,
        blank=True,
        null=True
    )
    published_date = models.DateTimeField(
        "дата публикации",
        default=timezone.now,
        blank=True,
        null=True
    )
    image = models.ImageField("главная фотография", upload_to="post/", null=True, blank=True)
    category = models.ManyToManyField(
        Category,
        verbose_name="Категория",
    )
    published = models.BooleanField("опубликовать?", default=True)
    sort = models.PositiveIntegerField('порядок', default=0)

    def __str__(self):
        return self.title



    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ['sort', '-published_date', ]

    def get_absolute_url(self):
        return reverse('blog:detail_post', kwargs={'slug': self.slug})

    def name_category(self):
        return '\n, \n '.join([str(child.name) for child in self.category.all()])

    name_category.short_description = 'Привязка к категориям'