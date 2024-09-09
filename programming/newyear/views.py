import datetime

from django.shortcuts import render
from django.urls import path


from . import views
# Create your views here.

def index(request):
    now = datetime.datetime.now()  # Define 'now' before using it
    return render(request, "newyear/index.html", {
        "newyear": now.month == 1 and now.day == 1
    })