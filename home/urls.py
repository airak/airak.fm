from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lastfm/', views.get_lastfm, name='get_lastfm')
]