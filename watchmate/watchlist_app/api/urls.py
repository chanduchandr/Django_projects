
from .views import get_all_movies, get_movies_by_pk
# from .views import get_all_movies
from django.urls import path

urlpatterns = [
    path('movies/', get_all_movies, name='movie-list'),  # URL for movie list
    path('movies/<int:pk>/', get_movies_by_pk, name='movie-by-id'),  # URL for movie list
]









