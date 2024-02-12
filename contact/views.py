from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def contact_lively(request):
    return HttpResponse("This would be the contact page")