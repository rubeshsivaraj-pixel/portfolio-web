from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    github_link = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Resume(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.title
