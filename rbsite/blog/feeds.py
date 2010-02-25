from django.contrib.syndication.feeds import Feed
from blog.models import Post

class LatestEntries(Feed):
	title = "redbrick.dcu.ie news updates"
	link = "http://www.redbrick.dcu.ie/news"
	description = "Updates on the latest news and announcements at redbrick.dcu.ie."

	def link(self, obj):
		return obj.get_absolute_url()

	def items(self):
		return Post.objects.all().order_by('-pub_date')[:10]