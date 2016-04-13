from django.shortcuts import render
from django.http import HttpResponse
from stormapp.models import Movie

def index(request):
	movies = Movie.objects.order_by('created_at')
	context = {'movies': movies}
	return render(request, 'stormapp/index.html', context)


def movie(request, movie_title):
	return HttpResponse("Filme Selected:  %s" % movie_title)


def order_by_gender(request, gender_name):
	return HttpResponse("Gender Page: %s" % gender_name)


def order_by_actor(request, actor_name):
	return HttpResponse("actor Page:  %s " % actor_name)