from django.conf import settings

class authPubcookie(object):
	def authenticate(self, username=None, password=None):
		# Check the username/password and return a User.
		pass
	
	def get_user(self, user_id):   
		try:    
			return User.objects.get(pk=user_id)    
		except User.DoesNotExist:
			return None
