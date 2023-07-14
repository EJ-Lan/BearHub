from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source project built by the community'
    }
]

def projects(requests):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(requests, 'projects/projects.html', context)

def project(requests, pk):
    projectObj = Project.objects.get(id=pk)
    return render(requests, 'projects/single-project.html', {'project':projectObj})
