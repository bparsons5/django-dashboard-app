from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def polls_index(request):
    return HttpResponse("Polls Index")
