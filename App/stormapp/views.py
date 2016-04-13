from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from stormapp.models import Movie, Gender

def index(request):
	movies = Movie.objects.order_by('title')
	context = {
		'header_content': 'Listagem de filmes',
		'movies': movies,
	}
	return render(request, 'stormapp/index.html', context)


def movie(request, slug):
	movie = Movie.objects.get(slug=slug)
	actors = movie.actors.all()
	genders = movie.genders.all()
	genders_str =', '.join([g.name for g in genders])
	actors_str =', '.join([g.name for g in actors])
	related_filmes = Movie.objects.filter(Q(genders=genders) | Q(actors=actors)).exclude(id=movie.id).distinct()
	context = {
		'header_content': movie.title,
		'movie': movie,
		'genders': genders_str,
		'actors': actors_str,
		'related_filmes': related_filmes,
	}
	return render(request, 'stormapp/movie.html', context)


def order_by_gender(request, gender_name):
	gender = Gender.objects.filter(name=gender_name)
	movies = Movie.objects.filter(genders=gender)
	context = {
		'header_content': gender_name,
		'movies': movies,
		'gender': gender
	}
	return render(request, 'stormapp/index.html', context)

def order_by_actor(request, actor_name):
	return HttpResponse("actor Page:  %s " % actor_name)
