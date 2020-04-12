from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

# Register your models here.
class DishInLine(admin.TabularInline):
    model = Restaurant.menu.through
    extra = 1
    # fields = ("name", "ingredients", "price", )


@admin.register(Dish)
class DishAdmin (admin.ModelAdmin):
    list_display = ('name', 'price', 'ingredients', "get_image")
    list_display_links = ('name',)
    readonly_fields = ("get_big_image",)

    def get_image (self, obj):
        if obj.image :
            return  mark_safe(f'<img src={obj.image.url} width=50px height=50px')
        else:
            return 'Нет картинки'

    def get_big_image (self, obj):
        if obj.image :
            return  mark_safe(f'<img src={obj.image.url} width=400px height=auto')
        else:
            return 'Нет картинки'

    get_image.short_description = "Картинка"
    get_big_image.short_description = "Картинка"


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'delivery_time', 'rating', 'price_level', 'category')
    list_display_links = ('name',)
    list_filter = ('rating',)
    inlines = [DishInLine]
    exclude = ('menu',)
    save_on_top = True
    readonly_fields = ("get_big_image",)

    def get_big_image (self, obj):
        if obj.image :
            return  mark_safe(f'<img src={obj.image.url} width=300px height=auto')
        else:
            return 'Нет картинки'

    fields = (('name', 'category'),
              ('delivery_time', 'rating', 'price_level'),
              ('image', 'get_big_image'))

    get_big_image.short_description = "Картинка"
