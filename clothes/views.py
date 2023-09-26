from django.views.generic import ListView, DetailView
from .models import Clothes

class ClothesListView(ListView):
    model = Clothes
    context_object_name = 'clothes_list'
    template_name = 'clothes/clothes_list.html'

class ClothesDetailView(DetailView):
    model = Clothes
    context_object_name = 'clothes'
    template_name = 'clothes/clothes_detail.html'