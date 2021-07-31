from django.db import models
from django.contrib.auth.models import User

class Color(models.Model):
    title = models.CharField(max_length=200, unique=True)
    color = models.TextField()
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title