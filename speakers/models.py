from django.contrib.auth.models import User
from django.db import models

from conference.models import Event, Track


class Speaker(User):
    notes = models.TextField()
    bio = models.TextField()
    rating = models.SmallIntegerField()
    twitter_handle = models.CharField(max_length=128)
    avatar = models.ImageField()
    international = models.BooleanField(default=False)


class SpeakerContent(models.Model):
    name = models.TextField()
    abstract = models.TextField()
    material = models.FileField()
    potential_track = models.ForeignKey(Track)
    main_speaker = models.ForeignKey(Speaker)
    secondary_speakers = models.ManyToManyField(Speaker, null=True, blank=True)

