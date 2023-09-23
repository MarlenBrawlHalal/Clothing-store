from django.urls import path

from .views import ClothesListView

urlpatterns = [
    path('', ClothesListView.as_view(), name='clothes_list'),
]