from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def blog_lively(request):
    return HttpResponse("This would be the blog page")