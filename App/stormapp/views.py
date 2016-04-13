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


def order_by_gender(request, slug):
	gender_obj = Gender.objects.filter(slug=slug)
	for gender in gender_obj:
		gender = gender
	movies = Movie.objects.filter(genders=gender)
	context = {
		'header_content': gender.name,
		'movies': movies,
	}

	return render(request, 'stormapp/index.html', context)

def order_by_actor(request, slug):
	actor = Gender.objects.filter(slug=slug)
	movies = Movie.objects.filter(actors=actor)
	context = {
		'header_content': actor.name,
		'movies': movies,
	}
	return render(request, 'stormapp/index.html', context)



# import pdb; pdb.set_trace()
