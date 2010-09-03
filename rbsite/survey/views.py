from rbsite.survey.models import Survey, Question
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from datetime import datetime

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

def thanks(request, survey_id):
	p = get_object_or_404(Survey, pk=survey_id)
	return render_to_response('survey/thanks.html', {'title': p.title})

def submit(request, survey_id):
	args = {}
	p = get_object_or_404(Survey, pk=survey_id)

	if request.method == 'POST':
		# Needed to have random/unique filenames
	 	now = datetime.now()
		dump_file = open("answers" + now.strftime("%Y-%m-%d-%H:%M:%S") + ".txt" , "w")

		#Keeps going until the number of questions specified
		for i in range(1, p.number_of_questions + 1):
			q = 'q' + str(i)
			dump_file.write("Question " + str(i) + '\n')
			qa = request.POST.getlist(q)

			#Writes the users input for this question in a human readable format
			for j in range(0, len(qa)):
				if j < len(qa) - 1:
					dump_file.write(qa[j] + ', ')
				else:
					dump_file.write(qa[j] + '\n\n')			
		dump_file.close()
	
	return HttpResponseRedirect(reverse('rbsite.survey.views.thanks', args=(p.id,)))
