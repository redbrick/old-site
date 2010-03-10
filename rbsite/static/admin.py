from django.contrib import admin
from rbsite.static.models import StaticPage

class StaticPageAdmin(admin.ModelAdmin):
	pass

admin.site.register(StaticPage, StaticPageAdmin)
