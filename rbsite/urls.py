from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from rbsite.blog.feeds import LatestEntries
import rbsite.settings


feeds = {
	'latest': LatestEntries,
}

# Auto discover admin stuff
admin.autodiscover()

urlpatterns = patterns('',
	# news posts.
	(r'^home/', include('rbsite.blog.urls')),
	
	(r'^news/', 'rbsite.blog.views.news'),
	
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

	# Comments
    (r'^comments/', include('django.contrib.comments.urls')),
    
    # feeds
    (r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),
    
    # static media, for dev only
    (r'media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':rbsite.settings.MEDIA_ROOT}),
    
    # Everything else gets passed through static page handler
    (r'', 'rbsite.static.views.static'),
)

