# Generated by Django 3.0.5 on 2021-03-15 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery_app', '0010_auto_20210315_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliveryorder',
            name='order_delivered',
            field=models.BooleanField(default=False, verbose_name='Заказ выполнен'),
        ),
    ]
