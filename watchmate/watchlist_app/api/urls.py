
# from .views import get_all_movies, get_movies_by_pk
from .views import WatchListListAV, WatchListDetailAV, StreamPlatformListAV, StreamPlatformDetailAV
# from .views import get_all_movies
from django.urls import path

urlpatterns = [
    path('WatchList/', WatchListListAV.as_view(), name='movie-list'),  # URL for movie list
    path('WatchList/<int:pk>/', WatchListDetailAV.as_view(), name='movie-by-id'),  # URL for movie list
    path('StreamPlatform/', StreamPlatformListAV.as_view(), name='movie-list'),  # URL for movie list
    path('StreamPlatform/<int:pk>/', StreamPlatformDetailAV.as_view(), name='movie-by-id'),  # URL for movie list
]









