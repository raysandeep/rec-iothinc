from django.db import models


class SN(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    register_number = models.CharField(max_length=100, blank=True, default='')
    email_id = models.CharField(max_length=253)
    phone = models.CharField(max_length=253)
    tech = models.BooleanField(default=False)
    mgt = models.BooleanField(default=False)
    design = models.BooleanField(default=False)
    otp = models.CharField(max_length=10)
    class Meta:
        ordering = ['created']
class QN(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    question = models.CharField(max_length=1000)
    o1 = models.CharField(max_length=200)
    o2 = models.CharField(max_length=200)
    o3 = models.CharField(max_length=200)
    o4 = models.CharField(max_length=200)
    co = models.CharField(max_length=200)
    class Meta:
        ordering = ['created']

