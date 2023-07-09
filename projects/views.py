from django.shortcuts import render
from django.http import HttpResponse

def projects(requests):
    return HttpResponse('Here are our projects')

def project(requests, pk):
    return HttpResponse('SINGLE PROJECT' + ' ' + str(pk))
