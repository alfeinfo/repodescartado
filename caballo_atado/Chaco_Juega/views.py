from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question
from django.http import Http404



def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template= loader.get_template('Chaco_Juega/index.html')
    context={
        'latest_question_list' : latest_question_list,
    }
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(template.render(context,request))

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'Chaco_Juega/index.html', context)

def detail(request, question_id):
    return HttpResponse("Estas viendo las preguntas %s." % question_id)

def results(request, question_id):
    response = "Estas viendo los resultados de las preguntas %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Estas votando sobre la pregunta %s." % question_id)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'Chaco_Juega/detail.html', {'question': question})

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'Chaco_Juega/detail.html', {'question': question})