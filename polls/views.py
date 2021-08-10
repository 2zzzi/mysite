"""
views.py의 가장 큰 역할은 request 를 받고 response를 해주는 역할이다.

"""
import datetime
from re import template

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView


from .models import Question, Choice

def index(request):
    #1. base view
    # return HttpResponse("hello world. youre at the polls index.")


    #2. Actually do something
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)

    #3. Use the template
    # lastest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list' : lastest_question_list}
    # return render(request, 'polls/index.html',context)

    #4 Using the shortcut - render
    if request.method == "GET":
        latest_question_list = Question.objects.order_by('-pub_date')[:5]
        template = loader.get_template('polls/index.html')
        context = {
            'latest_question_list' : latest_question_list,
        }
        return HttpResponse(template.render(context, request))

    if request.method == "POST":
        if request.POST['question']:
            Question.objects.create(question_text=request.POST['question'], pub_date=datetime.datetime.now())
            print("Success")
        return HttpResponseRedirect('/polls')
        

    
# class IndexView(generic.ListView):
#     template_name = 'polls/index.html'
#     context_object_name = 'latest_question_list'

#     def get_queryset(self):
#         return Question.objects.filter(
#             pub_date__lte=timezone.now() #lte는 less than equal
#         ).order_by('-pub_date')[:5]



    
def detail(request, question_id):
#     #1
#     #  try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     # return render(request, 'polls/detail.html',{'question':question})

#     #2
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/detail.html', {'question':question})

# class DetailView(generic.DetailView):
#     model = Question
#     template_name = "polls/detail.html"

#     def get_queryset(self):
#         return Question.objects.filter(pub_date__lte=timezone.now())

    

    

def results(request, question_id):
#     # 1.
    # return HttpResponse("You're looking at the results of question %s" % question_id)
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/results.html', {'question':question})


# class ResultView(DetailView):
#     model = Question
#     template_name = "polls/results.html"





def vote(request, question_id):
    #1.
    #  return HttpResponse("You're voting on quesetion %s" % question_id)
    
    #2.
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question' : question,
            'error_message':"You didn't select a choice",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        
        return HttpResponseRedirect(reverse('polls:results',args =(question.id,))) #post 로 호출된 경우어는 HttpResponesREdirect 로 리턴해준다. reserve는 뷰 함수에서 URL을 하드코딩하지 않게 해준다. 

