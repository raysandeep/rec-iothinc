from django.db import models



class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=100, blank=True, default='')
    fullname = models.CharField(max_length=100, blank=True, default='')
    counter = models.CharField(max_length=100, blank=True, default='')
    
    tech = models.BooleanField(default=False)
    mgt = models.BooleanField(default=False)
    design = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['created']