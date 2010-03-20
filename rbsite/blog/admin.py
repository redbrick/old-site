from django.contrib import admin
from rbsite.blog.models import Post

class PostAdmin(admin.ModelAdmin):
	fields = ('title','teaser',"large_teaser", 'body','show_on_homepage','position')
	list_display = ('title', 'author', 'pub_date')
	date_hierarchy = 'pub_date'
	
	#Set author automatically to the logged in user. 
	def save_model(self, request, obj, form, change):   
		if not change:
			obj.author = request.user
		
		if obj.show_on_homepage is True and obj.position == "":
			obj.position = "LL"
		
		obj.save()

admin.site.register(Post, PostAdmin)
