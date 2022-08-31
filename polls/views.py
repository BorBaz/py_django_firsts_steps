from django import template
from django.http import HttpResponse, Http404
from django.shortcuts import render

from polls.models import Question

VIEW_POLLS_DETAIL = "polls/detail.html"
VIEW_POLLS_INDEX = 'polls/index.html'


def index(request):
    # displays the latest 5 poll questions in the system, separated by commas, according to publication date
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_questions': latest_questions}

    return render(request, VIEW_POLLS_INDEX, context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exists")

    return render(request, "%s" % VIEW_POLLS_DETAIL, {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
