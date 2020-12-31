from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.


class User(models.Model):
    name = models.CharField('имя', max_length=100)
    last_name = models.CharField('фамилия', max_length=100)

    def __str__(self):
        return self.name


class Poll(models.Model):
    title = models.CharField('заголовок', max_length=100)
    description = models.CharField('описание', max_length=300)
    date_start = models.DateTimeField('дата начала опроса')
    date_end = models.DateTimeField('дата конца опроса')
    key = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Question(models.Model):
    type = models.CharField('тип вопроса', max_length=300)
    answer_items = ArrayField((ArrayField(models.CharField(max_length=10))))
    poll_id = models.ForeignKey(Poll, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Answer(models.Model):
    questions_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField('текст ответа', max_length=300)

    def __str__(self):
        return self.name
