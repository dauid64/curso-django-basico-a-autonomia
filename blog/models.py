from django.db import models

class Project(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    content = models.TextField()
    active = models.BooleanField(default=True)
    picture = models.ImageField(upload_to="projects/")
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='projects')
    tags = models.ManyToManyField('Tag', related_name='projects')

    def __str__(self):
        return self.title

class Category(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name