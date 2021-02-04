from django.shortcuts import render, get_object_or_404
from .models import Poll, PollQuestion, PollQuestionChoice
# Create your views here.


def polls_view(request):
    cntx = {
        'tests':  Poll.objects.all(),
    }
    return render(request, 'polls.html', context=cntx)


def pass_poll(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    print(poll)
    ctx = {
        'test': poll,
    }
    return render(request, 'pass_poll.html', ctx)
