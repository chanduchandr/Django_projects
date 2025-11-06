from watchlist_app.models import Movie
from .serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET', 'POST'])
def get_all_movies(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = MovieSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # ✅ must return Response
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        

@api_view(['GET', 'PUT','DELETE'])
def get_movies_by_pk(request, pk):
    if request.method == 'GET':
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    if request.method == 'PUT':
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    if request.method == 'DELETE':
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        

