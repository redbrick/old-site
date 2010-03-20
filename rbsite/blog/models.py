from django.db import models
from django.contrib.auth.models import User
from django.core.paginator import Paginator, InvalidPage, EmptyPage

# Create your models here.
class Post(models.Model):
	POST_POSITION_CHOICES = (
		('LL', 'Large Left Box'),
		('STR', 'Small Top Right Box'),
		('SMR', 'Small Middle Right Box'),
		('SBR', 'Small Bottom Right Box')
	)
	
	author = models.ForeignKey(User, related_name='posts')
	position = models.CharField(max_length=3,choices=POST_POSITION_CHOICES,blank=True)
	show_on_homepage = models.BooleanField()
	title = models.CharField(max_length=200)
	teaser = models.TextField()
	large_teaser = models.TextField()
	body = models.TextField() 
	pub_date = models.DateTimeField('Date Published', auto_now_add=True)
	up_date = models.DateTimeField('Date Updated', auto_now=True)
	
	def get_absolute_url(self):
		return "/home/%i/" % self.id 
	
	def __unicode__(self):
		return self.title