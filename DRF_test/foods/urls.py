from django.urls import path
from foods.views import FoodListApiView

urlpatterns = [
    path("foods/", FoodListApiView.as_view(), name="food-categories")
]
