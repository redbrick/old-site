import re
from django.template import RequestContext
from django.http import Http404
from django.shortcuts import render_to_response
from rbsite.static.models import StaticPage

def static(request):
	"""
	Finds a StaticPage based on the URI provided, and renders it.
	
	Throws a 404 if the page can't be found.
	"""
	
	request_uri = request.path
	
	# Sanitise URL - nothing but letters, numbers, underscores, dashes and forward slashes get through
	pattern = re.compile(r'[^a-zA-Z0-9/_-]')
	request_uri = pattern.sub('', request_uri)
	
	try:
		page = StaticPage.objects.filter(url__exact=request_uri)[0]
	except IndexError:
		raise Http404
	
	return render_to_response('static/static.html', {'page':page}, context_instance=RequestContext(request))
