from django import template
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from polls.models import Question, Choice

VIEW_POLLS_DETAIL = "polls/detail.html"
VIEW_POLLS_INDEX = 'polls/index.html'


def index(request):
    # displays the latest 5 poll questions in the system, separated by commas, according to publication date
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_questions': latest_questions}

    return render(request, VIEW_POLLS_INDEX, context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "%s" % VIEW_POLLS_DETAIL, {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        # Vuelve a ensenhar el formulario para preguntar
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "No has seleccionado una opcion",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
