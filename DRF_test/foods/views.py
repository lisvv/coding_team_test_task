from rest_framework import generics
from foods.serializers import FoodListSerializer
from foods.models import Food, FoodCategory
from django.db.models import Prefetch


class FoodListApiView(generics.ListAPIView):
    serializer_class = FoodListSerializer
    queryset = FoodCategory.objects.all().prefetch_related(
        Prefetch(
            "foods",
            queryset=Food.objects.filter(is_publish=True)))

    def get_queryset(self):
        foods = Food.objects.filter(is_publish=True)
        foods_category = FoodCategory.objects.filter(foods__in=[*foods]).distinct().prefetch_related(
            Prefetch("foods", queryset=Food.objects.filter(is_publish=True)),
            )
        return foods_category
