from django.db import models
from django.contrib.auth.models import AbstractUser
from phone_field import PhoneField

# Create your models here.


class User(AbstractUser):
    WHOISIT = [
        ('student', 'Stud'),  # Это реализовывается именно так, мы делаем типа селектор - вид для db/вид для внешнего
        ('teacher', 'Teach'),
    ]
    status = models.CharField(choices=WHOISIT, default='student', max_length=255)
    phone = PhoneField(blank=True, help_text='Contact phone number')
