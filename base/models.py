from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)

    avatar = models.ImageField(null=True, default="avatar.svg")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self): 
        return str(self.name) 
    

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) # many-to-one relationship, which sets host to null if user is deleted
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True) # many-to-one relationship, which sets topic to null if topic is deleted
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True) # many-to-many relationship, which allows for multiple users to participate in multiple rooms
    updated = models.DateTimeField(auto_now=True)  
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created', '-updated']

    def __str__(self): 
        return str(self.name)
  

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # many-to-one relationship, which deletes messages if user is deleted
    room = models.ForeignKey(Room, on_delete=models.CASCADE) # many-to-one relationship, which deletes messages if room is deleted
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created", "-updated"]

    def __str__(self):
        return str(self.body[0:50]) # return first 50 characters of message body