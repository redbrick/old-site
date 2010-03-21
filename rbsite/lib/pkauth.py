from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
import os

class PubcookieAuthBackend:
	def authenticate(self, username=None, password=None):
		try:
			assert username == os.environ['REMOTE_USER']
			assert os.environ['AUTH_TYPE'] == 'Pubcookie'
			assert os.environ['HTTPS'] == 'on' or os.environ['HTTPS'] == '1'
		except:
			return None
		
		try:
			user_obj = User.objects.filter(username__exact=username)[0]
		except:
			user_obj = User.objects.create_user(username, username + "@redbrick.dcu.ie", None)
			user_obj.save()
		
		return user_obj

def pkauth(request):
	response = HttpResponse()
	
	try:
		assert 'REMOTE_USER' in os.environ
		assert request.is_secure() is True
	except:
		return redirect("/")
	
	user_obj = authenticate(username=os.environ['REMOTE_USER'], password=None)
	if user is not None:
		login(request, user)
	
	return redirect("/")
