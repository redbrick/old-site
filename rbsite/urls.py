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
	(r'^news/', include('rbsite.blog.urls')),
    
	 # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

	# Comments
    (r'^comments/', include('django.contrib.comments.urls')),
    
    # feeds
    (r'^feeds/(?P<url>.*)/?$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),
    
    # static media, for dev only
    (r'media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':rbsite.settings.MEDIA_ROOT}),
   
	# homepage
	url(r'^/?$', 'rbsite.blog.views.index', name='blog'),
	
	# Pubcookie login helper
	url(r'/pkauth/mksession\.py/auth$', 'rbsite.lib.pkauth.pkauth'),

	# Everything else gets passed through static page handler
   (r'', 'rbsite.static.views.static'),
)

