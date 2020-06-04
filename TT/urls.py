from django.urls import path
from . import views

app_name='TT'
urlpatterns=[
    path('', views.index, name='index'),
]