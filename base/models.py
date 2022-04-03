from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    bio = models.TextField(null=True)

    avatar = models.ImageField(null=True, default="avatar.svg")
    created_on = models.DateTimeField(default=timezone.now)




class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(
        User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]

class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    subject = models.CharField(max_length=100)
    username = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    screenshot = models.ImageField(null=True, blank=True)

    class Meta:
        ordering = [ '-created']

    def __str__(self):
        return self.name

class ReadReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    subject = models.CharField(max_length=100)
    username = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    created = models.DateTimeField( null=True, blank=True)
    screenshot = models.ImageField(null=True, blank=True)

    class Meta:
        ordering = [ '-created']

    def __str__(self):
        return self.name
