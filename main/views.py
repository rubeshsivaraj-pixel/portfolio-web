from django.shortcuts import render
from .models import Project, Resume

def home(request):
    projects = Project.objects.all()
    resume = Resume.objects.first()
    return render(request, 'main/index.html', {
        'projects': projects,
        'resume': resume
    })
