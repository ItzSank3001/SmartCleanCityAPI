from django.db import models


# Create your models here.
from users.models import User

"""
class User(models.Model):
    #uid = models.IntegerField(primary_key=True, default='1', unique=True, blank=False)
    uid = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.IntegerField()
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    role = models.CharField(max_length=10)

    def __str__(self):
        return self.first_name

"""


class Complaint(models.Model):
    #cid = models.IntegerField(primary_key=True, default='1', unique=True, blank=False)
    cid = models.AutoField(primary_key=True)
    uid = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_id')
    did = models.CharField(max_length=50, blank=True, default='')
    #did = models.ForeignKey(User, on_delete=models.CASCADE, related_name='driver_id', blank=True, default='')
    description = models.CharField(max_length=100)
    date = models.DateField(auto_now=False, auto_now_add=True)
    photo = models.FileField(upload_to='images/')
    clat = models.FloatField()
    clong = models.FloatField()
    status = models.CharField(max_length=20, default='not assigned')


    def __str__(self):
        return self.description


class Bin(models.Model):
    #bid = models.IntegerField(primary_key=True, default='1', unique=True, blank=False)
    bid = models.AutoField(primary_key=True)
    alat = models.FloatField()
    along = models.FloatField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.address




"""
class Work(models.Model):
    wid = models.IntegerField(primary_key=True, default='1', unique=True, blank=False)
    description = models.CharField(max_length=100)
    bid = models.ForeignKey(Bin, on_delete=models.CASCADE)
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    priority = models.CharField(max_length=10)

    def __str__(self):
        return self.work_id

class Admin(models.Model):
    admin_id = models.CharField(max_length=10, default='admin', editable=False)
    admin_password = models.CharField(max_length=10, default='admin', editable=False)
"""
