# from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Restaurant, Dish
from rest_framework import generics
# from rest_framework.response import Response
# from rest_framework.views import APIView
from .serializers import RestaurantListSerializer, RestaurantDetailSerializer
import random

# Create your views here.


class RestaurantListView (ListView):
    model = Restaurant
    context_object_name = "restaurants"
    template_name = "delivery_app/restaurant_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # tanuki = get_object_or_404(Restaurant, name='Пицца-плюс')
        # context['tanuki_dishes'] = Dish.objects.filter(restaurant__pk=tanuki.pk)
        # context['dishes'] = Dish.objects.all()
        promo_backs = ['pizza', 'kebab', 'vegetables', 'sushi']
        promo_texts = ['Блюда из любимого ресторана привезет курьер в перчатках, маске и с антисептиком',
                       'Закажите шашлыки в любом ресторане до 10 мая и получите скидку по промокоду OMAGAD',
                       'Блюдо из ресторана привезут вместе с двумя подарочными книгами по фронтенду',
                       'Скидки на сеты до 30 мая по промокоду DADADA']
        random.seed()
        context['promo_back'] = promo_backs[random.randint(0, 3)]
        context['promo_text'] = promo_texts[random.randint(0, 3)]
        return context


class RestaurantDetailView (DetailView):
    model = Restaurant
    context_object_name = 'restaurant'
    template_name = 'delivery_app/restaurant_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = self.get_object()
        # context['dishes'] = Dish.objects.filter(restaurant__pk=obj.pk)
        context['dishes'] = obj.dishes.all()
        return context


class RestaurantListAPIVew (generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantListSerializer

# class RestaurantListAPIVew (APIView):
#
#     def get(self, request):
#         restaurants = Restaurant.objects.all()
#         serializer = RestaurantListSerializer(restaurants, many =  True)
#         return Response(serializer.data)


class RestaurantDetailAPIView (generics.RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantDetailSerializer

# class RestaurantDetailAPIView (APIView):
#
#     def get(self, request, pk):
#         restaurant = get_object_or_404(Restaurant, pk=pk)
#         serializer = RestaurantDetailSerializer(restaurant)
#         return Response(serializer.data)
