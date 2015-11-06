from django.contrib.auth.models import User
from django.db import models


class Sponsor(models.Model):
    name = models.CharField(max_length=1024)
    logo = models.ImageField()
    main_contact = models.ForeignKey(User)
    notes = models.TextField()


class SponsorshipConfiguration(models.Model):
    name = models.CharField(max_length=1024)


class SponsorshipOption(models.Model):
    name = models.CharField(max_length=1024)
    description = models.TextField()
    number_available = models.SmallIntegerField(default=1)
    cost = models.SmallIntegerField()
    option = models.ForeignKey(SponsorshipConfiguration)


class SponsorInterest(models.Model):
    sponsor = models.ForeignKey(Sponsor)
    option = models.ForeignKey(SponsorshipOption)
    status = models.CharField()


