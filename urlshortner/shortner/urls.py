from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),  # get url and create uid
    path('<str:pk>', views.go, name='go')  # catch uid and redirect to url
]
