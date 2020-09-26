from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


CATEGORY_CHOICES = [('food', 'Еда',), ('toys', 'Игрушки'), ('books', 'Книги'), ('clothes', 'Одежда'),
                    ('other', 'Другое')]


class Product(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, verbose_name='Название')
    category = models.CharField(max_length=100, null=False, blank= False, choices=CATEGORY_CHOICES,
                                verbose_name='Категория')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание')
    img = models.ImageField(null=False, blank=False, upload_to='product_pics', verbose_name='Картинка')

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
    rating = models.IntegerField(verbose_name='Оценка', validators=(MinValueValidator(1), MaxValueValidator(5),))

    def __str__(self):
        return f'{self.author} | {self.product}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

