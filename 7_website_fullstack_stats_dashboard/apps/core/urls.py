from django.urls import path

from apps.core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('chart/', views.chart, name='chart'),
    path('graph/', views.graph, name='graph'),
    path('languages/', views.languages, name='languages'),
    path('home_panels/', views.home_panels, name='home_panels'),
    path('panel_details/<int:panel_id>/', views.panel_details),
]
