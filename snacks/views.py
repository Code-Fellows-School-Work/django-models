from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import render
from .models import Snack

class AboutPageView(TemplateView):
    template_name = 'about.html'

class SnackListView(ListView):
    template_name = 'snack_list.html'
    model = Snack
    context_object_name = 'snacks'

class SnackDetailView(DetailView):
    template_name = 'snack_detail.html'
    model = Snack

def about_me(request):
    context = {
        'image_url': '.assets/PXL_20230816_231329155.MP.jpg',
    }
    return render(request, 'about_me.html', context)
