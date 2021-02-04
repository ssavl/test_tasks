from django.db import models

# Create your models here.

from auth_users.models import User


class Poll(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class PollQuestion(models.Model):
    text = models.TextField()
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='questions')

    def __str__(self):
        return self.text


class PollQuestionChoice(models.Model):
    is_correct = models.BooleanField()
    text = models.TextField(max_length=255)
    question = models.ForeignKey(PollQuestion, on_delete=models.CASCADE, related_name='choices')

    def __str__(self):
        return self.text


class PollQuestionAnswer(models.Model):
    question = models.ForeignKey(PollQuestion, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.ForeignKey(PollQuestionChoice, on_delete=models.CASCADE)

    def __str__(self):
        return f'Ответа студента {self.student}, на вопрос {self.question}'