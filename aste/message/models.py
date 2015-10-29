from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
	From=models.ForeignKey(User,related_name="From")
	To=models.ForeignKey(User,related_name="To")
	Text=models.TextField()
	data=models.DateTimeField(auto_now_add=True)
# Create your models here.
