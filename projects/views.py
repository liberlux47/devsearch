from django.shortcuts import render

def projects(request): 
    page = 'projects'
    msg = 'Hello, you are on the projects page!'
    return render(request, 'projects/projects.html', {'message': msg, 'page': page})

def project(request, pk):
    return render(request, 'projects/single-project.html')