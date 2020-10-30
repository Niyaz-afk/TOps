from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import DetailView, ListView
from .models import Movie, Actor
# Create your views here.

class MoviesView(ListView):
    model = Movie


class MovieDetailView(DetailView):

    model = Movie
    slug_field = 'url'


class ActorDetailView(DetailView):

    model = Actor
    template_name = 'movies/actor.html'
    slug_field = 'name'