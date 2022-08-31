from django import template
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from polls.models import Question

VIEW_POLLS_INDEX = 'polls/index.html'


def index(request):
    # displays the latest 5 poll questions in the system, separated by commas, according to publication date
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_questions': latest_questions}

    return render(request, VIEW_POLLS_INDEX, context)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
