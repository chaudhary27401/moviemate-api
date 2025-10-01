from moviemate.models import WatchList,StreamPlatform,Review
from moviemate.api.serializers import WatchListSerializer,StreamPlatformSerializer,ReviewSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from moviemate.api import permissions
from rest_framework.throttling import ScopedRateThrottle
from rest_framework import filters
from moviemate.api.pagination import WatchListPagination
# from rest_framework import pagination
class UserReview(generics.ListAPIView):
    serializer_class = ReviewSerializer
    def get_queryset(self):

        username = self.request.query_params.get('username',None)
        return Review.objects.filter(review_user__username = username)

class WatchListFilter(generics.ListAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer
    pagination_class = WatchListPagination

    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'platform__name']

class WatchListAV(APIView):
    permission_classes = [permissions.IsAdminOrReadOnly]
    def get(self,request):
        watch = WatchList.objects.all()
        serializer = WatchListSerializer(watch,many = True, context={'request': request})
        return Response(serializer.data)
    def post(self,request):
        serializer = WatchListSerializer(data= request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
class WatchDetailAV(APIView):
    permission_classes = [permissions.IsAdminOrReadOnly]
    def get(self,request,pk):
        try:
            item = WatchList.objects.get(pk=pk)
        except item.DoesNotExitst:
            return Response(status = status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(item)
        return Response(serializer.data)
    def put(self,request,pk):
        item = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(item,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    def delete(self,request,pk):
        item = WatchList.objects.get(pk=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class StreamPlatformListAV(APIView):
    permission_classes = [permissions.IsAdminOrReadOnly]
    def get(self,request):
        objects = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(objects,many = True)
        return Response(serializer.data)

    def post(self,request):
        serializer = StreamPlatformSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class StreamPlatformDetailAV(APIView):
    permission_classes = [permissions.IsAdminOrReadOnly]


    def get(self,request,pk):
        try:
            object = StreamPlatform.objects.get(pk=pk)

        except object.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = StreamPlatformSerializer(object)
        return Response(serializer.data)
    def put(self,request,pk):
        object = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(object,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    def delete(self,request,pk):
        object = StreamPlatform.objects.get(pk=pk)
        object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ReviewList(generics.ListCreateAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist = pk)

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.ReviewUserOrReadOnly]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    permission_classes = [IsAuthenticated]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = "review-detail"

class ReviewCreate(generics.CreateAPIView):

    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Review.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        movie = WatchList.objects.get(pk=pk)
        review_user = self.request.user
        review_queryset = Review.objects.filter(watchlist = movie, review_user = review_user)

        if review_queryset.exists():
            raise ValidationError("You have already reviewed the movie")
        serializer.save(watchlist= movie, review_user = review_user)








