from rbsite.survey.models import Survey, Question
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse

# Create your views here.

def index(request):
	args = {}
	
	try:
		latest_survey = Survey.objects.filter(show_on_poll_page=True).order_by('-pub_date')[0]
		args['latest_survey'] = latest_survey
	except:
		pass

	return render_to_response('survey/index.html', args)

def detail(request, survey_id):
	p = get_object_or_404(Survey, pk=survey_id)
	return render_to_response('survey/detail.html', {'survey': p})

def submit(request, survey_id):
	args = {}
	if request.method == 'POST':
		args['q1'] = request.POST.getlist('q1')
		args['q2'] = request.POST.getlist('q2')
		args['q3'] = request.POST.getlist('q3')
	return render_to_response('survey/test.html', args)
