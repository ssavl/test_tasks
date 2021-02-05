from django.shortcuts import render, get_object_or_404
from .models import Poll, PollQuestion, PollQuestionChoice, PollQuestionAnswer
from auth_users.models import User


def polls_view(request):
    cntx = {
        'tests':  Poll.objects.all(),
    }
    return render(request, 'polls.html', context=cntx)


def pass_poll(request, pk):
    if request.method == 'POST':
        print('-' * 80)
        print(request.POST)
        user = request.POST['user']
        answer = request.POST['flexRadioDefault']
        quest = get_object_or_404(Poll, pk=pk)
        quest_title = Poll.objects.get(title=quest)
        question = PollQuestion.objects.get(poll=quest_title)
        user_now = User.objects.get(username=user)
        choice = PollQuestionChoice(text=answer)
        print(f'data = {question}, {user_now}, {choice}')  # дебажный принт
        a = PollQuestionAnswer(question=question, student=user_now, answer=choice)
    poll = get_object_or_404(Poll, pk=pk)
    ctx = {
        'test': poll,
    }
    return render(request, 'pass_poll.html', ctx)
