from django.http import HttpResponse
from django.template import loader

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def index(request):
    template = loader.get_template('home/index.html')
    context = {
        'controller_name': 'Home Controller!!',
    }
    return HttpResponse(template.render(context, request))