from rest_framework import serializers
from .models import *


# Select all table from the database
class VideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Youtube_videos
        fields = "__all__"
