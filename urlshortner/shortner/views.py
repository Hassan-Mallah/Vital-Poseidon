from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


# get url and save it to DB
def create(request):
    pass