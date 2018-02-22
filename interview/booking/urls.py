from django.urls import path, re_path
from . import views


urlpatterns = [

    # the landing url
    path('', views.index, name='index'),
]
