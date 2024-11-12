from django.shortcuts import render
from django.http import  HttpResponse
from .models import product
# Create your views here.
def frst_view(request):
    return render(request,'index.html')
