from django.db import models

# Create your models here.

class Dish (models.Model):
    name = models.CharField (max_length=100, verbose_name='Название блюда')
    ingredients = models.TextField(verbose_name='Состав блюда')
    price = models.IntegerField(verbose_name='Цена блюда')
    image = models.ImageField(upload_to='images/dishes/%Y/%m/%d/', blank=True, verbose_name='Изображение блюда')
    restaurant = models.ForeignKey ("Restaurant", verbose_name="Ресторан", on_delete=models.CASCADE, default=1, related_name='dishes')

    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"

    def __str__ (self):
        return self.name


class Restaurant (models.Model):
    name = models.CharField (max_length=100, verbose_name='Название ресторана')
    delivery_time = models.IntegerField (verbose_name='Время доставки')
    rating = models.DecimalField (verbose_name='Рейтинг ресторана', max_digits=2, decimal_places=1)
    price_level = models.CharField (max_length=20, verbose_name='Уровень цен')
    category = models.CharField(max_length=100, verbose_name='Категория ресторана')
    image = models.ImageField (upload_to='images/restaurants/%Y/%m/%d/', blank=True, verbose_name="Изображение ресторана")
    # menu = models.ManyToManyField ('Dish', blank=True)

    class Meta:
        verbose_name = "Ресторан"
        verbose_name_plural = "Рестораны"

    def __str__ (self):
        return self.name