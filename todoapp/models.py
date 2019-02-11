from django.db import models

class Todo(models.Model):
	name = models.CharField(max_length=50)
	message = models.TextField()

	def __str__(self):
		return self.message[:20]

class UserRegister(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField()
	password = models.CharField(max_length=100)

	def __str__(self):
		return self.name

