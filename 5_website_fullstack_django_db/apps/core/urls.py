from django.urls import path

from apps.core import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('about/', views.about, name='about'),
    path('resources/', views.view_resources, name='resources'),
    path('blog-archive/', views.blog_archive, name='blog-archive'),    
    path('portfolio/', views.portfolio, name='portfolio'),
    path('contact/', views.contact, name='contact'),
    path('resume/', views.resume, name='resume'),
    path('blog-post-first/', views.blog_post_first, name='blog_post_first'),
    path('portfolio-details-client-grid/', views.portfolio_details_client_grid),
    path('portfolio-details-feast-and-west/', views.portfolio_details_feast_and_west),
    path('portfolio-details-github/', views.portfolio_details_github),
    path('portfolio-details-kickstart-coding-data-project-2/', views.portfolio_details_kickstart_coding_data_project_2),
    path('portfolio-details-kickstart-coding-data-project-3/', views.portfolio_details_kickstart_coding_data_project_3),
    path('portfolio-details-peach-and-pine/', views.portfolio_details_peach_and_pine),
    path('portfolio-details-rachel-anzalone/', views.portfolio_details_rachel_anzalone),
    path('portfolio-details-shayla-boyd-gill/', views.portfolio_details_shayla_boyd_gill),
    path('portfolio-details-west-trade/', views.portfolio_details_west_trade),
    path('services/', views.services, name='services'),
    path('github/', views.github, name='github'),

]