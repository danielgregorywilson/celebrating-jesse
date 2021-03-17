import datetime

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _


class Memory(models.Model):
    class Meta:
        abstract = True

    uploaded_by = models.ForeignKey("auth.User", verbose_name=_("uploaded by"), on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField("datetime uploaded", auto_now_add=True)
    title = models.TextField(blank=True)
    description = models.TextField(blank=True)
    date = models.DateField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    approved = models.BooleanField(default=False)


class Story(Memory):
    class Meta:
        verbose_name = _("Story")
        verbose_name_plural = _("Stories")

    story = models.TextField(blank=True, null=True)


class Image(Memory):
    class Meta:
        verbose_name = _("Image")
        verbose_name_plural = _("Images")

    image = models.ImageField(upload_to="images")


class Video(Memory):
    class Meta:
        verbose_name = _("Video")
        verbose_name_plural = _("Videos")

    video = models.FileField(upload_to="videos")


class Audio(Memory):
    class Meta:
        verbose_name = _("Audio")
        verbose_name_plural = _("Audios")

    audio = models.FileField(upload_to="audio")