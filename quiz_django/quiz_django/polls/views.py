from django.shortcuts import render, get_object_or_404
from .models import Poll, PollQuestion, PollQuestionChoice, PollQuestionAnswer
from auth_users.models import User
# import the logging library
import logging
from django.contrib import messages



# Get an instance of a logger
logger = logging.getLogger(__name__)

def polls_view(request):
    cntx = {
        'tests':  Poll.objects.all(),
    }
    return render(request, 'polls.html', context=cntx)


def pass_poll(request, pk):
    if request.method == 'POST':
        answer = request.POST['flexRadioDefault']
        logger.info(f'user{request.user} submitted data: {request.POST}')
        quest = get_object_or_404(Poll, pk=pk)
        quest_title = Poll.objects.get(title=quest)
        question = PollQuestion.objects.get(poll=quest_title)
        choice = PollQuestionChoice(text=answer)
        PollQuestionAnswer.objects.create(question=question, student=request.user, answer=choice)
        messages.success('Тест пройден')
        return render(request, 'pass_poll.html', {})
    poll = get_object_or_404(Poll, pk=pk)
    ctx = {
        'test': poll,
    }
    return render(request, 'pass_poll.html', ctx)
