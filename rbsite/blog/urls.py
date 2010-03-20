from django.conf.urls.defaults import *
from models import Post


queryset = {'queryset': Post.objects.order_by('-pub_date')}

urlpatterns = patterns('',
	url('^/?$', 'rbsite.blog.views.news'),
	url('^(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail', queryset, name="post"),
)

