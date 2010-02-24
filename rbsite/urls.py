from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	# news posts.
	(r'^news/', include('rbsite.blog.urls')),
	
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

	# Comments
    (r'^comments/', include('django.contrib.comments.urls')),
)
