from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Authority(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    pin=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    AUTHUSER = models.OneToOneField(User, on_delete=models.CASCADE)

class BoatRegister(models.Model):
    ownername = models.CharField(max_length=100)
    ownernumber = models.CharField(max_length=100)
    owneremail = models.CharField(max_length=100)
    ownerplace = models.CharField(max_length=100)
    boatphoto = models.CharField(max_length=100)
    boatregistrationid=models.CharField(max_length=100)
    boatlicensephoto=models.CharField(max_length=100)
    AUTHORITY = models.ForeignKey(Authority, on_delete=models.CASCADE)

class Users(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    photo = models.CharField(max_length=100)
    BOATREGISTER = models.ForeignKey(BoatRegister, on_delete=models.CASCADE)
    AUTHUSER = models.OneToOneField(User, on_delete=models.CASCADE)


class Rescue(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    photo=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    AUTHUSER=models.OneToOneField(User,on_delete=models.CASCADE)




class Alert(models.Model):
    date=models.DateField()
    status=models.CharField(max_length=100)
    detection=models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    time=models.TimeField()


class Complaint(models.Model):
    date=models.CharField(max_length=100)
    complaint=models.CharField(max_length=100)
    reply=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    USERS=models.ForeignKey(Users,on_delete=models.CASCADE)



class Notification(models.Model):
    date=models.CharField(max_length=100)
    notification=models.CharField(max_length=100)


class Help(models.Model):
    USERS = models.ForeignKey(Users, on_delete=models.CASCADE)
    date=models.DateField()
    time=models.TimeField()
    status=models.CharField(max_length=100)
    latitude=models.CharField(max_length=100)
    longitude=models.CharField(max_length=100)
    RESCUETEAM=models.ForeignKey(Rescue,on_delete=models.CASCADE)


class Zone(models.Model):
    latitude=models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    AUTHORITY=models.ForeignKey(Authority,on_delete=models.CASCADE)


class Banschedule(models.Model):
    ZONE=models.ForeignKey(Zone,on_delete=models.CASCADE)
    from_date=models.CharField(max_length=100)
    to_date=models.CharField(max_length=100)
    status=models.CharField(max_length=100)


class Fine(models.Model):
    date=models.CharField(max_length=100)
    amount=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    USERS=models.ForeignKey(Users,on_delete=models.CASCADE)
