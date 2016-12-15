from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),  ##when url entered go to index function in views.py
]
