from django.shortcuts import render
from django.views.generic.base import View
from .models import Movie
# Create your views here.


class MovieView(View):
    """Список фильмов"""

    def get(self,request):
        movies = Movie.objects.all()
        return render(request,'movies/movie_list.html')