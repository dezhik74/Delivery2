from rest_framework import serializers

from .models import Restaurant, Dish


class DishListSerializer (serializers.ModelSerializer):

    class Meta:
        model =Dish
        fields = ('__all__')

class RestaurantListSerializer (serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields =('name', 'delivery_time', 'rating', 'price_level', 'category', 'image')


class RestaurantDetailSerializer (serializers.ModelSerializer):

    dishes = DishListSerializer (many=True, read_only=True)
    # dishes = serializers.SlugRelatedField(slug_field='name', many=True, read_only=True)
    # dishes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # dishes = serializers.HyperlinkedRelatedField(view_name='dish-detail', many=True, read_only=True)

    class Meta:
        model = Restaurant
        fields = ('name', 'delivery_time', 'rating', 'price_level', 'category', 'image', 'dishes')

