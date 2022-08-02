import datetime
from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    title = models.CharField('Наименование', max_length=100)
    slug = models.SlugField('url', max_length=100)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        verbose_name = "Категория новостей"
        verbose_name_plural = "Категории новостей"

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})

    def __str__(self):
        return self.title


class ProductList(models.Model):
    title = models.CharField('Название', max_length=500, db_index=True)
    slug = models.SlugField("url", max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', null=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    price = models.DecimalField('Цена', max_digits=6, decimal_places=2)
    published = models.BooleanField('Опубликовать?', default=True)
    published_date = models.DateTimeField("Дата публикации", default=datetime.datetime.now(), blank=True, null=True)

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def get_absolute_url(self):
        return reverse('detail_post', kwargs={'category': self.category.slug, 'slug': self.slug})


class ProductDetail(models.Model):
    title = models.CharField('Заголовок', max_length=500)
    slug = models.SlugField("url", max_length=100)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    description = models.TextField('Описание', max_length=5000)
    quantity = models.BooleanField('Колличество', default=1)
    price = models.DecimalField('Цена', max_digits=6, decimal_places=2)
