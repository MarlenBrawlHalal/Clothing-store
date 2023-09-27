from django.urls import path

from .views import ClothesListView, ClothesDetailView, SearchResultsListView

urlpatterns = [
    path('', ClothesListView.as_view(), name='clothes_list'),
    path('<uuid:pk>/', ClothesDetailView.as_view(), name='clothes_detail'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
]