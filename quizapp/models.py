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
    q_id= models.IntegerField()
    question = models.CharField(max_length=1000)
    o1 = models.CharField(max_length=200)
    o2 = models.CharField(max_length=200)
    o3 = models.CharField(max_length=200)
    o4 = models.CharField(max_length=200)
    co = models.CharField(max_length=200)
    class Meta:
        ordering = ['created']
class Questions(models.Model):
    CAT_CHOICES = (
    ('recur1','IoThinC Recuirtment'),
    ('recur2','IoThinc Recuirtment2')
    )
    question = models.CharField(max_length = 250)
    optiona = models.CharField(max_length = 100)
    optionb = models.CharField(max_length = 100)
    optionc = models.CharField(max_length = 100)
    optiond = models.CharField(max_length = 100)
    answer = models.CharField(max_length = 100)
    catagory = models.CharField(max_length=20, choices = CAT_CHOICES)

    class Meta:
        ordering = ('-catagory',)

    def __str__(self):
        return self.question


class results(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    regis = models.CharField(max_length = 100)
    marks = models.CharField(max_length = 100)
    class Meta:
        ordering = ['created']
