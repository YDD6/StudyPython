# from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string

# Create your views here.
def index(request):
    html = render_to_string("index2.html")
    return HttpResponse(html)