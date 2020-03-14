# Generated by Django 3.0.4 on 2020-03-13 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='Заголовок')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Текст')),
                ('image', models.ImageField(blank=True, null=True, upload_to='post/', verbose_name='главная фотография')),
                ('edit_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата редактирования')),
                ('published_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации')),
                ('published', models.BooleanField(default=True, verbose_name='Опубликовать?')),
                ('slug', models.CharField(max_length=100, unique=True, verbose_name='url')),
            ],
            options={
                'verbose_name': 'Страница',
                'verbose_name_plural': 'Страницы',
                'unique_together': {('slug',)},
            },
        ),
    ]
