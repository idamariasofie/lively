from django.shortcuts import render
from django.views import generic
from .models import Recipe

# Create your views here.
class PostList(generic.ListView):
    queryset = Recipe.objects.all().order_by("-created_on")
    template_name = "post_list.html"