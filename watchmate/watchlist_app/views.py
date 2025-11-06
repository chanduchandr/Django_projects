# from django.shortcuts import render
# from .models import Movie
# from django.http import JsonResponse

# def get_all_movies(request):
#     movies = Movie.objects.all()
#     data = {
#         'Movies': list(movies.values())
#         }
#     return JsonResponse(data) 

# def get_movies_by_pk(request, pk):
#     movie = Movie.objects.get(pk=pk)
#     data = {
#         'name':movie.name,
#         'discription':movie.discreption
#     }
#     return JsonResponse(data)
