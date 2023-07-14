from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm

def projects(requests):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(requests, 'projects/projects.html', context)

def project(requests, pk):
    projectObj = Project.objects.get(id=pk)
    return render(requests, 'projects/single-project.html', {'project':projectObj})

def createProject(request):
    form = ProjectForm()
    context = {'form': form}
    return render(request, "projects/project_form.html", context)