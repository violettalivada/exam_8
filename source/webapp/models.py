from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Avg, Sum

CATEGORY_CHOICES = [('food', 'Еда',), ('toys', 'Игрушки'), ('books', 'Книги'), ('clothes', 'Одежда'),
                    ('other', 'Другое')]

RATING_RANGE = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5)
]


class Product(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, verbose_name='Название')
    category = models.CharField(max_length=100, null=False, blank= False, choices=CATEGORY_CHOICES,
                                verbose_name='Категория')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание')
    img = models.ImageField(null=True, blank=True, upload_to='product_pics', verbose_name='Картинка')

    def __str__(self):
        return f'{self.pk}. {self.name}'

    class Meta:
        verbose_name = 'Товар/Услуга'
        verbose_name_plural = 'Товары/Услуги'


class Review(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_DEFAULT, default=1, related_name='products',
                               verbose_name='Автор')
    product = models.ForeignKey('webapp.Product', related_name='reviews', on_delete=models.CASCADE,
                                verbose_name='Товар')
    text = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Отзыв')
    rating = models.IntegerField(verbose_name='Оценка', choices=RATING_RANGE)

    def __str__(self):
        return f'{self.author} | {self.product}'

    def get_avg_rating(self):
        return self.rating

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

