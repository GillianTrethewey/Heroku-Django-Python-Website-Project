from django.urls import path

from apps.core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('chart/', views.chart, name='chart'),
    path('graph/', views.graph, name='graph'),
    path('languages/', views.languages, name='languages'),
]
