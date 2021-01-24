# Generated by Django 2.2.10 on 2021-01-23 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Youtube_videos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('video_id', models.CharField(max_length=255)),
                ('video_title', models.CharField(max_length=1000)),
                ('video_description', models.CharField(blank=True, max_length=10000, null=True)),
                ('video_publishedDateTime', models.DateTimeField()),
                ('video_thumb_urls', models.URLField()),
                ('channel_id', models.CharField(max_length=1000)),
                ('channel_title', models.CharField(max_length=1000)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
