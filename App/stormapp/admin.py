from django.contrib import admin

# Register your models here.
from .models import Movie, Gender, Actor
admin.site.register(Movie)
admin.site.register(Gender)
admin.site.register(Actor)
