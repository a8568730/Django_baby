from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse 
from django.http import Http404
from polls.models import Question
from django.template import RequestContext, loader
# Create your views here.

def index(request):
	# 從資料庫讀出最近的問題
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	# 找出用來顯示index的模板
	template = loader.get_template('polls/index.html')
	context = RequestContext(request, {
		'latest_question_list': latest_question_list
	})
	return HttpResponse(template.render(context))
def detail(request, question_id):
# 	try:
# 		question = Question.objects.get(pk=question_id)
# 	except Question.DoesNotExist:
# 		raise Http404
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question':question})
def results(request, question_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response % question_id)
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)