from django.contrib.syndication.feeds import Feed
from rbsite.blog.models import Post

class LatestEntries(Feed):
	title = "redbrick.dcu.ie news updates"
	link = "/news/"
	description = "Updates on the latest news and announcements at redbrick.dcu.ie."
	
	def items(self):
		return Post.objects.order_by('-pub_date')[:10]
	
	def item_link(self, item):
		if not item:
			return ""
		return "/news/%i/" % item.id
