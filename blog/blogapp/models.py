from django.db import models
from django.contrib.auth.models import User


class Blog_Post(models.Model):
    image = models.ImageField(upload_to = 'img')
    title = models.CharField(max_length = 200)
    body = models.TextField()
    slug = models.SlugField()
    writer = models.ForeignKey(User, on_delete = models.CASCADE)
    created_on = models.DateTimeField(auto_now = True)