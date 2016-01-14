from django.db import models
from tinymce.models import HTMLField
from django.conf import settings
from django.utils import timezone


class Subject(models.Model):
    name = models.CharField(max_length=254)
    description = HTMLField()

    def __unicode__(self):
        return self.name


class Thread(models.Model):
    name = models.CharField(max_length=254)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='threads')
    subject = models.ForeignKey(Subject, related_name='threads')
    created_at = models.DateTimeField(default=timezone.now)


class Posts(models.Model):
    thread = models.ForeignKey(Thread, related_name='posts')
    comment = HTMLField(blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts')
    created_at = models.DateTimeField(default=timezone.now)


class Poll(models.Model):
    question = models.TextField()
    thread = models.OneToOneField(Thread, null=True)


class PollSubject(models.Model):
    name = models.CharField(max_length=256)
    poll = models.ForeignKey(Poll, related_name='subjects')


class Vote(models.Model):
    poll = models.ForeignKey(Poll, related_name="votes")
    subject = models.ForeignKey(PollSubject, related_name="votes")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="votes")
