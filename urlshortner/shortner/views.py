from django.shortcuts import render
import uuid
from .models import Url
from django.http import HttpResponse


# Create your views here.
def index(request: HttpResponse):
    return render(request, 'index.html')


# get url and save it to DB
def create(request: HttpResponse):
    if request.method == 'POST':
        url = request.POST['link']
        # generate short id and shorten it to 5
        uid = str(uuid.uuid4())[:5]

        # create and save url record
        new_url = Url(link=url, uuid=uid)
        new_url.save()

        return HttpResponse(uid)