from django.db import models
from django.shortcuts import reverse


class Dish(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название блюда')
    ingredients = models.TextField(verbose_name='Состав блюда')
    price = models.IntegerField(verbose_name='Цена блюда')
    image = models.ImageField(upload_to='images/dishes/%Y/%m/%d/', blank=True, verbose_name='Изображение блюда')
    restaurant = models.ForeignKey("Restaurant", verbose_name="Ресторан", on_delete=models.CASCADE, default=1,
                                   related_name='dishes')

    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название ресторана')
    delivery_time = models.IntegerField(verbose_name='Время доставки')
    rating = models.DecimalField(verbose_name='Рейтинг ресторана', max_digits=2, decimal_places=1)
    price_level = models.CharField(max_length=20, verbose_name='Уровень цен')
    category = models.CharField(max_length=100, verbose_name='Категория ресторана')
    image = models.ImageField(upload_to='images/restaurants/%Y/%m/%d/', blank=True,
                              verbose_name="Изображение ресторана")

    class Meta:
        verbose_name = "Ресторан"
        verbose_name_plural = "Рестораны"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('restaurant_detail_url', kwargs={'pk': self.pk})


class PromoBox(models.Model):
    promo_text = models.TextField(verbose_name='Текст промо')
    promo_color = models.CharField(max_length=100, verbose_name='Цвет подложки промо и позиционирование')
    promo_img = models.ImageField(upload_to='images/promo/', blank=True, verbose_name='Картинка промо (png)')

    class Meta:
        verbose_name = "Промо постер"
        verbose_name_plural = "Промо постеры"

    def __str__(self):
        return self.promo_text[0:50] + '...'


class DeliveryOrderItem(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название блюда')
    price = models.IntegerField(verbose_name='Цена блюда')
    count = models.IntegerField(verbose_name='Количество')
    order = models.ForeignKey("DeliveryOrder", verbose_name='Заказ', on_delete=models.CASCADE, related_name='items')

    class Meta:
        verbose_name = "Строка заказа"
        verbose_name_plural = "Строки заказа"

    def __str__(self):
        return self.name + ' -> ' + str(self.count) + ' шт.'


class DeliveryOrder(models.Model):
    address = models.CharField(max_length=500, verbose_name='Адрес доставки')
    phone = models.CharField(max_length=20, verbose_name='Телефон для связи')
    name = models.CharField(max_length=20, verbose_name='Имя')
    comment = models.CharField(max_length=500, verbose_name='Комментарий')
    order_date = models.DateTimeField(auto_now_add=True, verbose_name='Заказ создан')
    order_delivered = models.BooleanField(verbose_name='Заказ выполнен', default=False)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    @staticmethod
    def save_in_base(common_order_data, basket):
        order = DeliveryOrder(address=common_order_data['address'],
                              phone=common_order_data['phone'],
                              name=common_order_data['name'],
                              comment=common_order_data['comment'])
        order.order_delivered = False
        order.save()
        for item in basket.values():
            order_item = DeliveryOrderItem(name=item['name'],
                                           price=item['price'],
                                           count=item['count'])
            order_item.order = order
            order_item.save()
