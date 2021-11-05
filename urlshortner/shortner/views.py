from django.shortcuts import render, redirect
import uuid
from .models import Url
from django.http import HttpResponse


# Create your views here.
def index(request: HttpResponse):
    return render(request, 'index.html')


# get url, create uid and save it to DB
def create(request: HttpResponse):
    if request.method == 'POST':
        url = request.POST['link']
        # generate short id and shorten it to 5
        uid = str(uuid.uuid4())[:5]

        # create and save url record
        new_url = Url(link=url, uuid=uid)
        new_url.save()

        return HttpResponse(uid)


# catch uid and redirect to url
def go(request: HttpResponse, pk):
    # get one or none
    try:
        # get link from DB
        url_details = Url.objects.get(uuid=pk)
        link = url_details.link

        # check if link starts with http
        if not link.startswith('http'):
            link = 'http://' + link
        return redirect(link)
    except Exception as e:
        print(e)
        return HttpResponse(pk + ' not found, plz double check')
