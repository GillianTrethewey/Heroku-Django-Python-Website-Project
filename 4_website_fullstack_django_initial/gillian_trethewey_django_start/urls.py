"""gillian_trethewey_django_start URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function view s
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from website import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path('about/', views.about),
    path('blog-archive/', views.blog_archive),    
    path('portfolio/', views.portfolio),
    path('contact/', views.contact),
    path('resume/', views.resume),
    path('blog-post-first/', views.blog_post_first),
    path('portfolio-details-client-grid/', views.portfolio_details_client_grid),
    path('portfolio-details-feast-and-west/', views.portfolio_details_feast_and_west),
    path('portfolio-details-github/', views.portfolio_details_github),
    path('portfolio-details-kickstart-coding-data-project-2/', views.portfolio_details_kickstart_coding_data_project_2),
    path('portfolio-details-kickstart-coding-data-project-3/', views.portfolio_details_kickstart_coding_data_project_3),
    path('portfolio-details-peach-and-pine/', views.portfolio_details_peach_and_pine),
    path('portfolio-details-rachel-anzalone/', views.portfolio_details_rachel_anzalone),
    path('portfolio-details-shayla-boyd-gill/', views.portfolio_details_shayla_boyd_gill),
    path('portfolio-details-west-trade/', views.portfolio_details_west_trade),
    path('services/', views.services),
    path('github/', views.github),

]