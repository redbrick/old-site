from django.contrib import admin
from rbsite.survey.models import Survey, Question

class QuestionsInline(admin.StackedInline):
	model = Question

class SurveyAdmin(admin.ModelAdmin):
	fields = ('title', 'show_on_poll_page')
	list_display = ('title', 'pub_date', 'show_on_poll_page')
	date_hierarchy = 'pub_date'
	inlines = [QuestionsInline]

admin.site.register(Survey, SurveyAdmin)
