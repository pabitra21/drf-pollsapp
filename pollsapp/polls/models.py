from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Track(models.Model):
    name = models.CharField(max_length=100, blank=True)

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    tracks = models.ForeignKey(Track, related_name='questions', on_delete=models.CASCADE)
    pub_date = models.DateTimeField(blank=True,null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Answer(models.Model):
    questions=models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    correct_answer = models.CharField(max_length=200)