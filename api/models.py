from django.db import models
from datetime import datetime


# Database Table
class Youtube_videos(models.Model):
    video_id = models.CharField(blank=False, null=False, max_length=255)

    video_title = models.CharField(blank=False, null=False, max_length=1000)

    video_description = models.CharField(blank=True,
                                         null=True,
                                         max_length=10000)

    video_publishedDateTime = models.DateTimeField()

    video_thumb_urls = models.URLField()

    channel_id = models.CharField(blank=False, null=False, max_length=1000)

    channel_title = models.CharField(blank=False, null=False, max_length=1000)

    created = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True,
    )

    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         self.timestamp = datetime.utcnow()
    #     return super(Youtube_videos, self).save(*args, **kwargs)
