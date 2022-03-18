from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.views.decorators.http import require_GET, require_POST

from polls.models import Question
import logging

logger = logging.getLogger('django')


@require_GET
def index(request: HttpRequest):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {
        "latest_question_list": latest_question_list,
    }
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)


@require_POST
def detail(request: HttpRequest, question_id: int):
    match request:
        case HttpRequest(htmx=_):
            detail_template = "polls/htmx_detail.html"
        case HttpRequest():
            detail_template = "polls/detail.html"
        case _:
            raise ValueError("Unknown request type")

    question = get_object_or_404(Question, pk=question_id)
    return render(request, detail_template, {"question": question})


@require_GET
def results(request: HttpRequest, question_id: int):
    response = "You're looking at the results of question {}."
    return HttpResponse(response.format(question_id))


@require_GET
def vote(request: HttpRequest, question_id: int):
    return HttpResponse("You're voting on question {}.".format(question_id))
