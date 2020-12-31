from django.contrib import admin

# Register your models here.

from .models import User, Poll, Question, Answer

admin.site.register(User)
admin.site.register(Poll)
admin.site.register(Question)
admin.site.register(Answer)


