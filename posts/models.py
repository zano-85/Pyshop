from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=200)
    timestamp = models.DateTimeField()
    image = models.CharField(max_length=2083)



