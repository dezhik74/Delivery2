from django.urls import path
from .views import RestaurantListView, RestaurantDetailView, RestaurantListAPIVew, RestaurantDetailAPIView, Cart

urlpatterns = [
    path('', RestaurantListView.as_view(), name='restaurants_list_url'),
    path('restaurants/<int:pk>/', RestaurantDetailView.as_view(), name='restaurant_detail_url'),
    path('add-dish/<int:pk_restaurant>/<int:pk_dish>/', RestaurantDetailView.add_dish_to_basket,
         name='dish_to_basket_url'),
    path('cart/', Cart.as_view(), name='cart'),
    path('api/v1/restaurants/', RestaurantListAPIVew.as_view()),
    path('api/v1/<int:pk>/', RestaurantDetailAPIView.as_view()),
    ]

