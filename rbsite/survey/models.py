from django.db import models

# Create your models here.

class Survey(models.Model):
	title = models.CharField(max_length=200)
	show_on_poll_page = models.BooleanField()
	pub_date = models.DateTimeField('Date Published', auto_now_add=True)
	up_date = models.DateTimeField('Date Updated', auto_now=True)

	def get_absolute_url(self):
		return '/surveys/%i' % self.id

	def __unicode__(self):
		return self.title

class Question(models.Model):
	INPUT_TYPE_CHOICES = (
		('text', 'Text Box'),
		('radio', 'Radio Buttons'),
		('checkbox', 'Checkboxes'),
		('textarea', 'Text Area'),
		('select', 'Drop Down Select'),
	)
	
	survey = models.ForeignKey(Survey)
	question = models.TextField(help_text="Ask the question here")
	input_type = models.CharField(max_length=50, choices=INPUT_TYPE_CHOICES)
	option1 = models.CharField(max_length=250, help_text="Only to be used with radio, checkbox and select input options", blank=True)
	option2 = models.CharField(max_length=250, help_text="Only to be used with radio, checkbox and select input options", blank=True)
	option3 = models.CharField(max_length=250, help_text="Only to be used with radio, checkbox and select input options", blank=True)
	option4 = models.CharField(max_length=250, help_text="Only to be used with radio, checkbox and select input options", blank=True)
	option5 = models.CharField(max_length=250, help_text="Only to be used with radio, checkbox and select input options", blank=True)

	def __unicode__(self):
		return self.question
