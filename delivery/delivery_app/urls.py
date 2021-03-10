from django.urls import path
from .views import RestaurantListView, RestaurantDetailView, RestaurantListAPIVew, RestaurantDetailAPIView, Cart, \
    MakeOrder

urlpatterns = [
    path('', RestaurantListView.as_view(), name='restaurants_list_url'),
    path('restaurants/<int:pk>/', RestaurantDetailView.as_view(), name='restaurant_detail_url'),
    path('add-dish/<int:pk_restaurant>/<int:pk_dish>/', RestaurantDetailView.add_dish_to_basket,
         name='dish_to_basket_url'),
    path('cart/', Cart.as_view(), name='cart'),
    path('cart-dish-sub/<int:pk_dish>/', Cart.cart_dish_sub, name='cart_dish_sub_url'),
    path('cart-dish-add/<int:pk_dish>/', Cart.cart_dish_add, name='cart_dish_add_url'),
    path('cart-clear/', Cart.cart_clear, name='cart_clear_url'),
    path('make-order/', MakeOrder.as_view(), name='make_order'),
    path('api/v1/restaurants/', RestaurantListAPIVew.as_view()),
    path('api/v1/<int:pk>/', RestaurantDetailAPIView.as_view()),
    ]

