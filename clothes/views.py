from typing import Any
from django.db.models import Q
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Clothes

class ClothesListView(LoginRequiredMixin, ListView):
    model = Clothes
    context_object_name = 'clothes_list'
    template_name = 'clothes/clothes_list.html'
    login_url = 'account_login'

class ClothesDetailView(LoginRequiredMixin, DetailView):
    model = Clothes
    context_object_name = 'clothes'
    template_name = 'clothes/clothes_detail.html'
    login_url = 'account_login'

class SearchResultsListView(ListView):
    model = Clothes
    context_object_name = 'clothes_list'
    template_name = 'clothes/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Clothes.objects.filter(
            Q(title__icontains=query)
        )