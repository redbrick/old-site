from django.conf.urls.defaults import *
from models import Post
from blog.feeds import LatestEntries

feeds = {
	'latest': LatestEntries,
}

queryset = {'queryset': Post.objects.order_by('-pub_date')}
urlpatterns = patterns('',#'django.views.generic.list_detail',
	url('^$', 'rbsite.blog.views.index'),#, queryset, name="blog"),    
	url('^(?P<object_id>\d+)/$', 'object_detail', queryset, name="post"),
 	(r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),
)

