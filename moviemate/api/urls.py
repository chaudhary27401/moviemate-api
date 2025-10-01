# from django import urls
from django.urls import path
from moviemate.api.views import WatchDetailAV,WatchListAV,StreamPlatformListAV,StreamPlatformDetailAV,ReviewList,ReviewDetail, ReviewCreate,UserReview,WatchListFilter
from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "MovieMate API is running!"})
urlpatterns = [
    path("", home),
    path("list/", WatchListAV.as_view(), name = "watch-list"),
    path("<int:pk>", WatchDetailAV.as_view(),name = "watch-detail"),
    path("stream/",StreamPlatformListAV.as_view(), name = 'streamplatform-list' ),
    path("stream/<int:pk>/", StreamPlatformDetailAV.as_view(), name = 'streamplatform-detail'),
    path("stream/<int:pk>/review-create/", ReviewCreate.as_view(), name = "review-create"),
    path("stream/<int:pk>/review/", ReviewList.as_view(), name = 'review-list'),
    path("stream/review/<int:pk>/", ReviewDetail.as_view(), name = "review-detail"),
    path("reviews/",UserReview.as_view(),name = "review-user"),
    path("watch-filter",WatchListFilter.as_view(), name = 'watch-filter')
]

