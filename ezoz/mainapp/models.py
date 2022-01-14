from operator import mod
from re import M
from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.


class Background(models.Model):
    video = models.FileField()


class Video(models.Model):
    video = models.FileField()


class FirstSlider(models.Model):
    pictures = models.ImageField()


class SecondSlider(models.Model):
    pictures = models.ImageField()


class FirstComment(models.Model):
    thik_font = models.TextField()
    thin_font = models.TextField()


class SecondComment(models.Model):
    thik_font = models.TextField()
    thin_font = models.TextField()



class CentralPicture(models.Model):
    central_picture = models.ImageField()


class Gallery(models.Model):
    pictures = models.ImageField()


class MainNumber(models.Model):
    phone = models.CharField(max_length=13)


class Number(models.Model):
    phone = models.CharField(max_length=13)