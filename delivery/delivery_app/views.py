from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from .models import Restaurant, Dish
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RestaurantListSerializer, RestaurantDetailSerializer

# Create your views here.


class RestaurantListView (ListView):
    model = Restaurant
    context_object_name = "restaurants"
    template_name = "delivery_app/restaurant_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # tanuki = get_object_or_404(Restaurant, name='Пицца-плюс')
        # context['tanuki_dishes'] = Dish.objects.filter(restaurant__pk=tanuki.pk)
        context['dishes'] = Dish.objects.all()
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


class RestaurantListAPIVew (APIView):

    def get(self, request):
        restaurants = Restaurant.objects.all()
        serializer = RestaurantListSerializer(restaurants, many =  True)
        return Response(serializer.data)

class RestaurantDetailAPIView (APIView):

    def get(self, request, pk):
        restaurant = get_object_or_404(Restaurant, pk=pk)
        serializer = RestaurantDetailSerializer(restaurant)
        return Response(serializer.data)
