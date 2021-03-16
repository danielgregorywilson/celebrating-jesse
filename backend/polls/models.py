import datetime

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Memory(models.Model):
    class Meta:
        abstract = True

    uploaded_by = models.ForeignKey("auth.User", verbose_name=_("uploaded by"), on_delete=models.CASCADE)
    title = models.TextField(blank=True)
    description = models.TextField(blank=True)
    date = models.DateField(blank=True, null=True)
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