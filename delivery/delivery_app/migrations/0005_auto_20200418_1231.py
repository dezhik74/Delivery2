# Generated by Django 3.0.5 on 2020-04-18 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivery_app', '0004_auto_20200414_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='restaurant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='restaurant', to='delivery_app.Restaurant', verbose_name='Ресторан'),
        ),
    ]
