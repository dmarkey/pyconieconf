from django.db import models

from speakers.models import SpeakerContent


class Venue(models.Model):
    name = models.CharField(max_length=1024)
    description = models.TextField()
    address = models.TextField()
    sponsor = models.ForeignKey("sponsors.Sponsor")


class VenueSchedule(models.Model):
    name = models.CharField()


class VenueResource(models.Model):
    name = models.CharField()
    capacity = models.SmallIntegerField(default=50)


class Track(models.Model):
    name = models.CharField()
    details = models.TextField()


class Event(models.Model):
    name = models.CharField(max_length=1024)
    logo = models.ImageField()
    details = models.TextField()
    start_day = models.DateField()
    duration = models.SmallIntegerField(default=1)
    open_for_sponsors = models.BooleanField(default=False)
    open_for_speakers = models.BooleanField(default=False)
    tracks = models.ManyToManyField(Track)
    #ticket_configuration = models.BooleanField(default=False)
    schedule = models.ForeignKey(VenueSchedule)
    sponsorship_configuration = models.ForeignKey("sponsors.SponsorshipConfiguration")


class SlotType(models.Model):
    name = models.CharField(max_length=1024)


class EventSlot(models.Model):
    resource = models.ForeignKey(VenueResource)
    start_time = models.DateTimeField()
    duration = models.SmallIntegerField()
    speaker_content = models.ManyToManyField(SpeakerContent, null=True, blank=True)
    slot_type = models.ForeignKey(SlotType)


