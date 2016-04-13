from django.shortcuts import render
from django.http import HttpResponse
from stormapp.models import Movie

def index(request):
	movies = Movie.objects.order_by('title')
	context = {
		'header_content': 'Listagem de filmes',
		'movies': movies,
	}
	return render(request, 'stormapp/index.html', context)


def movie(request, slug):
	movie = Movie.objects.get(slug=slug)
	context = {
		'header_content': movie.title,
		'movie': movie,
	}
	return render(request, 'stormapp/movie.html', context)


def order_by_gender(request, gender_name):
	return HttpResponse("Gender Page: %s" % gender_name)


def order_by_actor(request, actor_name):
	return HttpResponse("actor Page:  %s " % actor_name)
