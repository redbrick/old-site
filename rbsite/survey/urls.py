from django.conf.urls.defaults import *

urlpatterns = patterns('rbsite.survey.views',
	(r'^$', 'index'),
	(r'^(?P<survey_id>\d+)/$', 'detail'),
	(r'^(?P<survey_id>\d+)/submit/$', 'submit'),
	(r'^(?P<survey_id>\d+)/thanks/$', 'thanks'),
)
