from django.conf.urls.defaults import *
from models import Post
queryset = {‘queryset’: Post.objects.order_by('-pub_date')}

urlpatterns = patterns('',
	url('^$', 'object_list', queryset, name="posts"),    
	url('^(?P<object_id>\d+)/$', 'object_detail', queryset, name="post"),
)

