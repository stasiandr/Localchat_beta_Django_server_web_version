from django.db import models

class ChatPoint(models.Model):
	chat_name = models.CharField(max_length=30)
	messages = models.TextField()
	x = models.CharField(max_length=19)
	y = models.CharField(max_length=19)

