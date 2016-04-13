import os

from django.db import models

def get_image_path(instance, filename):
	return os.path.join('static/stormapp/movie_pictures', str(instance.category), filename)


class Movie(models.Model):
	title = models.CharField(max_length=200)
	sinopse = models.TextField(max_length=2000)
	created_at = models.DateTimeField(auto_now_add=True)
	picture = models.ImageField(upload_to='static/stormapp/movie_pictures', blank=True, null=True)
	slug = models.SlugField(unique=True)
	actors = models.ManyToManyField('Actor')
	genders = models.ManyToManyField('Gender')
	releated_filmes = models.ManyToManyField('self')

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