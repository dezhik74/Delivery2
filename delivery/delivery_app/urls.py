from django.urls import path
from .views import RestaurantListView, RestaurantDetailView, RestaurantListAPIVew, RestaurantDetailAPIView

urlpatterns = [
    path ('', RestaurantListView.as_view(), name='restaurants_list_url'),
    path ('restaurants/<int:pk>/', RestaurantDetailView.as_view(), name='restaurant_detail_url'),
    path ('api/v1/restaurants/', RestaurantListAPIVew.as_view()),
    path ('api/v1/<int:pk>/', RestaurantDetailAPIView.as_view()),
    ]

