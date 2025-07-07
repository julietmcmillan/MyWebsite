from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('education/', views.education, name='education'),
    path('projects/', views.projects, name='projects'),
    path('interests/', views.interests, name='interests'),
    path('contact/', views.contact, name='contact'),
] 