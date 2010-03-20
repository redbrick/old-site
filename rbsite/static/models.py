from django.db import models

class StaticPage(models.Model):
	section = models.CharField(max_length=255)
	url = models.CharField(max_length=255)
	title = models.CharField(max_length=255)
	content = models.TextField()
	
	class Admin:
		pass
	
	def __unicode__(self):
		return self.url

