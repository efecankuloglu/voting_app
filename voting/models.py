from django.db import models
from django.utils import timezone

import datetime

class ActiveManager(models.Manager):
    def get_queryset(self):
        all_polls = Question.objects.filter(active=True)
        for i in all_polls:
            if timezone.now() > i.publish + datetime.timedelta(minutes=i.duration):
                i.active = False
                i.save()
        return super(ActiveManager, self).get_queryset().filter(active=True)


class Question(models.Model):
    title = models.CharField(max_length=100)
    publish = models.DateTimeField(default=timezone.now)
    duration = models.IntegerField(default=0)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title[:50]       

    objects = models.Manager()
    actives = ActiveManager()
        
        
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text[:50]