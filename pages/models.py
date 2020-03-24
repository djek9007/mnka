from django.db import models
from django.urls import get_script_prefix, reverse
from django.utils.encoding import iri_to_uri
from django.utils.translation import gettext_lazy as _
from sorl.thumbnail import ImageField, get_thumbnail

class Pages(models.Model):
    """Страницы"""
    title = models.CharField(_("Заголовок"), max_length=500)
    text = models.TextField(_("Текст"), blank=True, null=True)
    image = models.ImageField("главная фотография", upload_to="post/", null=True, blank=True)
    edit_date = models.DateTimeField(
        _("Дата редактирования"),
        auto_now=True,
        blank=True,
        null=True
    )
    published_date = models.DateTimeField(_("Дата публикации"), blank=True, null=True)
    published = models.BooleanField(_("Опубликовать?"), default=True)
    slug = models.CharField("url", max_length=100, unique=True)

    def __str__(self):
        return self.title



    def get_absolute_url(self):
        return reverse('pages:page', kwargs={'slug': self.slug})
        
    # @property
    # def thumbnail(self):
    #     if self.image:
    #         return get_thumbnail(self.image, '730x509', quality=80)
    #     return None

    class Meta:
        verbose_name = _("Страница")
        verbose_name_plural = _("Страницы")
        unique_together = ('slug',)