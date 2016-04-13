import os

from django.db import models

def get_image_path(instance, filename):
	return os.path.join('static/stormapp/movie_pictures', str(instance.category), filename)


class Movie(models.Model):
	title = models.CharField(max_length=200)
	sinopse = models.TextField(max_length=800)
	created_at = models.DateTimeField(auto_now_add=True)
	picture = models.ImageField(upload_to='stormapp/static/stormapp/movie_pictures', blank=True, null=True)

	def __str__(self):
		return self.title



class Actor(models.Model):
	name =  models.CharField(max_length=200)

	def __str__(self):
		return self.name




class Gender(models.Model):
	name =  models.CharField(max_length=200)

	def __str__(self):
		return self.name