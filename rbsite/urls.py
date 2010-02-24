from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
#	(r'^home/', include('rbsite.blog.urls')),
	(r'^', include('posts.urls')),
	
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
