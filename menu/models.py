from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.models import Site
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Menu(models.Model):
    """Позиция меню"""
    name = models.CharField(_("Название"), max_length=255)
    status = models.BooleanField(_("Только для зарегистрированных"), default=False)
    published = models.BooleanField(_("Отображать?"), default=True)

    def __str__(self):
        return self.name

    def items(self):
        return self.menuitem_set.all()

    class Meta:
        verbose_name = _("Меню")
        verbose_name_plural = _("Меню")


class MenuItem(MPTTModel):
    """Элементы меню"""
    title = models.CharField(_("Название пункта меню на сайте"), max_length=255)
    slug = models.CharField(_("Url"), max_length=255)
    parent = TreeForeignKey(
        'self',
        verbose_name=_("Родительский пункт"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    menu = models.ForeignKey('Menu', verbose_name=_("Меню"), on_delete=models.CASCADE)
    sort = models.PositiveIntegerField(_('Порядок'), default=0)
    published = models.BooleanField(_("Отображать?"), default=True)

    def get_absolute_url(self):
        return reverse('blog:category', kwargs={'category_slug': self.slug.split('/')[1]})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Пункт меню")
        verbose_name_plural = _("Пункты меню")

    class MPTTMeta:
        order_insertion_by = ('sort',)
