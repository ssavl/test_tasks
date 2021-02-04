from django.contrib import admin
from .models import Poll, PollQuestion, PollQuestionAnswer, PollQuestionChoice


admin.site.register(Poll)
admin.site.register(PollQuestion)
admin.site.register(PollQuestionAnswer)
admin.site.register(PollQuestionChoice)