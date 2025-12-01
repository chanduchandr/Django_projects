
# from .views import get_all_movies, get_movies_by_pk
from .views import (WatchListListAV, WatchListDetailAV, StreamPlatformListAV, 
                    StreamPlatformDetailAV, ReviewDetailAV, ReviewListAV, 
                    ReviewCreate, WatchListListVS)
# from .views import get_all_movies
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('stream', WatchListListVS, basename='movie-by-id')

# urlpatterns = [
#     # path('WatchList/', WatchListListAV.as_view(), name='movie-list'),  # URL for movie list
#     # path('WatchList/<int:pk>/', WatchListDetailAV.as_view(), name='movie-by-id'),  # URL for movie list
#     path('',include(router.urls)),
#     path('streamplatform/', StreamPlatformListAV.as_view(), name='streamplatform-list'),
#     path('streamplatform/<int:pk>/', StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),
#     path('StreamPlatform/<int:pk>/review/', ReviewListAV.as_view(), name='review-list'),  # URL for movie list
#     path('StreamPlatform/<int:pk>/review-create', ReviewCreate.as_view(), name='review-create'),  # URL for movie list
#     path('StreamPlatform/review/<int:pk>/', ReviewDetailAV.as_view(), name='review-by-id'),  # URL for movie list
# ]


urlpatterns = [
    # StreamPlatform
    # path('stream/', StreamPlatformListAV.as_view(), name='stream-list'),
    # path('stream/<int:stream_id>/', StreamPlatformDetailAV.as_view(), name='stream-detail'),
    path('', include(router.urls)),

    # WatchList under a specific StreamPlatform
    path('stream/<int:stream_id>/watch/', WatchListListAV.as_view(), name='watch-list'),
    path('stream/<int:stream_id>/watch/<int:watch_id>/', WatchListDetailAV.as_view(), name='watch-detail'),
    path('stream/<int:pk>/review-create', ReviewCreate.as_view(), name='review-create'),  # URL for movie list
    # Reviews under a specific WatchList
    path('stream/<int:stream_id>/watch/<int:watch_id>/review/', ReviewListAV.as_view(), name='review-list'),
    path('stream/<int:stream_id>/watch/<int:watch_id>/review/<int:review_id>/', ReviewDetailAV.as_view(), name='review-detail'),
]








