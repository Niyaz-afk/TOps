from django.urls import path
from . import views

urlpatterns = [
    path('', views.MoviesView.as_view()),
    path('<slug:slug>', views.MovieDetailView.as_view(), name='movie_detail'),
    path('actor/<str:slug>', views.ActorDetailView.as_view(), name='actor_detail')
]