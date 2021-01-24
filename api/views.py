from django.shortcuts import render
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import *
from .serializers import *

# Rest FrameWork
from rest_framework import generics
from rest_framework.pagination import CursorPagination


# Pagination
# Tweak according to your own needs
class ResultsPagination(CursorPagination):
    page_size = 25
    page_size_query_param = 'page_size'
    max_page_size = 50


class YoutubeItems(generics.ListAPIView):
    search_fields = ['video_title', 'video_description']
    filter_backends = (filters.SearchFilter, DjangoFilterBackend,
                       filters.OrderingFilter)
    filterset_fields = ['channel_id', 'channel_title']
    ordering = ('-video_publishedDateTime')
    queryset = Youtube_videos.objects.all()
    serializer_class = VideosSerializer
    pagination_class = ResultsPagination
