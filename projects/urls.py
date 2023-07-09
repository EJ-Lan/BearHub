from django.urls import path
from . import views


urlpatterns = [
        path('projects/', views.projects, name="projects"),
    path('project/<str:pk>/', views.project, name="project"),
]