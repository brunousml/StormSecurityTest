from django.db import models

class Movie(models.Model):
	title = models.CharField(max_length=200)
	sinopse = models.CharField(max_length=800)
	picture = models.TextField()

class Actor(models.Model):
	name =  models.CharField(max_length=200)

class Gender(models.Model):
	name =  models.CharField(max_length=200)