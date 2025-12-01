from watchlist_app.models import WatchList, StreamPlatform, Review
from .serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrReadOnly
from .permissions import AdminOrReadOnly
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


class WatchListListVS(viewsets.ModelViewSet):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    """
    A simple ViewSet for listing or retrieving users.
    """
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = StreamPlatformSerializer
    queryset = StreamPlatform.objects.all()
    
    # def list(self, request):
    #     queryset = StreamPlatform.objects.all()
    #     serializer = StreamPlatformSerializer(queryset, many=True, context={'request': request})
    #     return Response(serializer.data)

    # def retrieve(self, request, pk=None):
    #     queryset = StreamPlatform.objects.all()
    #     user = get_object_or_404(queryset, pk=pk)
    #     serializer = StreamPlatformSerializer(user, context={'request': request})
    #     return Response(serializer.data)


class WatchListListAV(APIView):
    """Handles GET (list all WatchLists) and POST (create WatchList)"""
    permission_classes = [IsAdminOrReadOnly]
    def get(self, request, stream_id):
        watchlists = WatchList.objects.filter(platform_id=stream_id)
        serializer = WatchListSerializer(watchlists, many=True)
        return Response(serializer.data)

    def post(self, request, stream_id):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(platform_id=stream_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WatchListDetailAV(APIView):
    """Handles GET (single WatchList), PUT (update), and DELETE (remove)"""
    
    permission_classes = [IsAdminOrReadOnly]

    def get_object(self, stream_id, watch_id):
        return get_object_or_404(WatchList, id=watch_id, platform_id=stream_id)

    def get(self, request, stream_id, watch_id):
        watch = self.get_object(stream_id, watch_id)
        serializer = WatchListSerializer(watch)
        return Response(serializer.data)

    def put(self, request, stream_id, watch_id):
        watch = self.get_object(stream_id, watch_id)
        serializer = WatchListSerializer(watch, data=request.data)
        if serializer.is_valid():
            serializer.save(platform_id=stream_id)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, stream_id, watch_id):
        watch = self.get_object(stream_id, watch_id)
        watch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class StreamPlatformListAV(APIView):
    """Handles GET (list all WatchLists) and POST (create WatchList)"""

    def get(self, request):
        platform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platform, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StreamPlatformDetailAV(APIView):
    """Handles GET (single WatchList), PUT (update), and DELETE (remove)"""
    
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'error': 'WatchList not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = StreamPlatformSerializer(platform, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except platform.DoesNotExist:
            return Response({'error': 'WatchList not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = StreamPlatformSerializer(platform, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except platform.DoesNotExist:
            return Response({'error': 'WatchList not found'}, status=status.HTTP_404_NOT_FOUND)

        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
 
    
class ReviewCreate(generics.CreateAPIView):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    # def get_queryset(self):
    #     pk = self.kwargs['pk']
    #     return Review.objects.filter(watchlist=pk)
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        movie = WatchList.objects.get(pk=pk)
        
        review_user = self.request.user
        review_queryset = Review.objects.filter(watchlist = movie, review_user=review_user)

        if movie.number_rating == 0:
            movie.avg_rating = serializer.validated_data['rating']
        else:
            
            movie.avg_rating = (movie.avg_rating + serializer.validated_data['rating'])/2    
        movie.number_rating = movie.number_rating + 1
        
        movie.save()
        serializer.save(watchlist=movie, review_user=review_user)
        
        if review_queryset.exists():
            raise ValidationError('This user review is already exists')
        else:
            serializer.save(watchlist = movie, review_user = review_user)
    
    
class ReviewListAV(generics.ListCreateAPIView):
    
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = ReviewSerializer
    def get_queryset(self):
        watch_id = self.kwargs['watch_id']
        return Review.objects.filter(watchlist_id=watch_id)

    def perform_create(self, serializer):
        watch_id = self.kwargs['watch_id']
        review_user = self.request.user
        watch = get_object_or_404(WatchList, id=watch_id)

        # Prevent duplicate reviews by the same user
        if Review.objects.filter(watchlist=watch, review_user=review_user).exists():
            raise ValidationError("You have already reviewed this movie.")
        
       
        serializer.save(watchlist=watch, review_user=review_user)
    
class ReviewDetailAV(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    lookup_field = 'id'  # or 'pk' (default)
    lookup_url_kwarg = 'review_id'

    def get_queryset(self):
        watch_id = self.kwargs['watch_id']
        return Review.objects.filter(watchlist_id=watch_id)

    
# class ReviewListAV(
#     mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView
# ):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    

# class ReviewDetailAV(
#     mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView, mixins.RetrieveModelMixin
# ):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)  
    
    
    
    
    
    
    

# class ReviewListAV(APIView):
#     """Handles GET (list all WatchLists) and POST (create WatchList)"""

#     def get(self, request):
#         review = Review.objects.all()
#         serializer = ReviewSerializer(review, many=True, context={'request': request})
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ReviewSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# class ReviewDetailAV(APIView):
#     """Handles GET (single WatchList), PUT (update), and DELETE (remove)"""

#     def get(self, request, pk):
#         try:
#             review = Review.objects.get(pk=pk)
#         except review.DoesNotExist:
#             return Response({'error': 'WatchList not found'}, status=status.HTTP_404_NOT_FOUND)

#         serializer = ReviewSerializer(review, context={'request': request})
#         return Response(serializer.data)

#     def put(self, request, pk):
#         try:
#             review = Review.objects.get(pk=pk)
#         except review.DoesNotExist:
#             return Response({'error': 'WatchList not found'}, status=status.HTTP_404_NOT_FOUND)

#         serializer = ReviewSerializer(review, data=request.data, context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         try:
#             review = Review.objects.get(pk=pk)
#         except review.DoesNotExist:
#             return Response({'error': 'WatchList not found'}, status=status.HTTP_404_NOT_FOUND)

#         review.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
# @api_view(['GET', 'POST'])
# def get_all_WatchLists(request):
#     if request.method == 'GET':
#         WatchLists = WatchList.objects.all()
#         serializer = WatchListSerializer(WatchLists, many=True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         serializer = WatchListSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)  # ✅ must return Response
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        

# @api_view(['GET', 'PUT','DELETE'])
# def get_WatchLists_by_pk(request, pk):
#     if request.method == 'GET':
#         WatchList = WatchList.objects.get(pk=pk)
#         serializer = WatchListSerializer(WatchList)
#         return Response(serializer.data)
#     if request.method == 'PUT':
#         WatchList = WatchList.objects.get(pk=pk)
#         serializer = WatchListSerializer(WatchList, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#     if request.method == 'DELETE':
#         WatchList = WatchList.objects.get(pk=pk)
#         WatchList.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
        
        

