from django.urls import path

from counter_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('counter', views.counter, name='counter'),
]
