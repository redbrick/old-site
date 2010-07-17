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

	# Automatically filter to the logged in users posts
	# And show them all if the user is a superuser.
	def queryset(self, request):
		if request.user.is_superuser:
			return Post.objects.all()
		return Post.objects.filter(author=request.user)

	# Ensure that the user is allowed to edit that object.
	# User is only allowed to edit the posts if they own it
	# Superuser can only edit a users posts, not create one.
	def has_change_permission(self, request, obj=None):
		has_class_permission = super(PostAdmin, self).has_change_permission(request, obj)
		if not has_class_permission:
			return False
		if obj is not None and not request.user.is_superuser and request.user.id != obj.author.id:
			return False
		return True

admin.site.register(Post, PostAdmin)
