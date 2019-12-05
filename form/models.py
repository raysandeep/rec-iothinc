from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    reg = models.CharField(max_length=100, blank=True, default='')
    skills = models.IntegerField()
    capability = models.IntegerField()
    depth = models.IntegerField()
    tech = models.BooleanField(default=False)
    design = models.BooleanField(default=False)
    manage = models.BooleanField(default=False)
    final_bool = models.BooleanField(default=False)
    final_review = models.TextField()
    class Meta:
        ordering = ['created']