from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Dish, Restaurant, PromoBox


class DishInLine(admin.StackedInline):
    # model = Restaurant.menu.through
    model = Dish
    extra = 3
    # fields = ("name", "ingredients", "price", )
    readonly_fields = ("get_big_image",)
    fields = (('name', 'price'),
              'ingredients',
              ('image', "get_big_image"))

    def get_big_image (self, obj):
        if obj.image :
            return  mark_safe(f'<img src={obj.image.url} width=200px height=auto')
        else:
            return 'Нет картинки'

    get_big_image.short_description = "Картинка"



@admin.register(Dish)
class DishAdmin (admin.ModelAdmin):
    list_display = ('name', 'price', 'ingredients')
    # list_display = ('name', 'price', 'ingredients', "get_image")
    list_display_links = ('name',)
    readonly_fields = ("get_big_image",)
    save_on_top = True
    #
    # def get_image (self, obj):
    #     if obj.image :
    #         return  mark_safe(f'<img src={obj.image.url} width=50px height=50px')
    #     else:
    #         return 'Нет картинки'

    def get_big_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src={obj.image.url} width=400px height=auto')
        else:
            return 'Нет картинки'

    # get_image.short_description = "Картинка"
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
            return mark_safe(f'<img src={obj.image.url} width=300px height=auto')
        else:
            return 'Нет картинки'

    fields = (('name', 'category'),
              ('delivery_time', 'rating', 'price_level'),
              ('image', 'get_big_image'))

    get_big_image.short_description = "Картинка"


@admin.register(PromoBox)
class PromoBoxAdmin(admin.ModelAdmin):
    readonly_fields = ("get_big_image",)

    def get_big_image(self, obj):
        if obj.promo_img:
            return mark_safe(f'<img src={obj.promo_img.url} width=400px height=auto')
        else:
            return 'Нет картинки'

    get_big_image.short_description = "Картинка"


admin.site.site_title = "Доставка из ресторанов"
admin.site.site_header = "Доставка из ресторанов"
