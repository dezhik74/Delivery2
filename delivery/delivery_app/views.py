# from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView

from .forms import DeliveryForm
from .models import Restaurant, Dish, PromoBox, DeliveryOrder
from .basket import basket_add, basket_total, get_basket_as_dict, basket_sub, basket_clear
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
        random.seed()
        context['promo'] = PromoBox.objects.get(pk=random.randint(1, len(PromoBox.objects.all())))
        context['cart_total'] = basket_total(self.request)
        return context


class RestaurantDetailView (DetailView):
    model = Restaurant
    context_object_name = 'restaurant'
    template_name = 'delivery_app/restaurant_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = self.get_object()
        context['dishes'] = obj.dishes.all()
        context['cart_total'] = basket_total(self.request)
        return context

    @staticmethod
    def add_dish_to_basket(request, pk_restaurant, pk_dish):
        dish = get_object_or_404(Dish, pk=pk_dish)
        restaurant = get_object_or_404(Restaurant, pk=pk_restaurant)
        basket_add(request, dish)
        return redirect(restaurant)


class Cart(TemplateView):
    template_name = "delivery_app/basket.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_total'] = basket_total(self.request)
        context['cart'] = get_basket_as_dict(self.request)
        return context

    @staticmethod
    def cart_dish_sub(request, pk_dish):
        basket_sub(request, pk_dish)
        return redirect('cart')

    @staticmethod
    def cart_dish_add(request, pk_dish):
        dish = get_object_or_404(Dish, pk=pk_dish)
        basket_add(request, dish)
        return redirect('cart')

    @staticmethod
    def cart_clear(request):
        basket_clear(request)
        return redirect('restaurants_list_url')


class MakeOrder(TemplateView):
    template_name = "delivery_app/make_order.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_total'] = basket_total(self.request)
        context['cart'] = get_basket_as_dict(self.request)
        context['form'] = DeliveryForm()
        return context

    def post(self, request):
        form = DeliveryForm(request.POST)
        if form.is_valid():
            # print(get_basket_as_dict(request))
            # print(form.cleaned_data)
            DeliveryOrder.save_in_base(form.cleaned_data, get_basket_as_dict(request))
            basket_clear(request)
            return redirect('thank_you_url')


class ThankYouView(TemplateView):
    template_name = "delivery_app/thanks.html"


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
