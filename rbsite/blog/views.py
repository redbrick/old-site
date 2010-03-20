from django.http import HttpResponse
from django.shortcuts import render_to_response
from rbsite.blog.models import Post
from django.core.paginator import Paginator, InvalidPage, EmptyPage

# Create your views here.
def index(request):
	args = {}
	
	for p in ['LL','STR','SMR','SBR']:
		try:
			post = Post.objects.filter(show_on_homepage=True).filter(position__exact=p).order_by('-up_date')[0]
			args[p] = post
		except:
			pass
	
	return render_to_response('blog/index.html',args)

def news(request):
	post_list = Post.objects.all()
	paginator = Paginator(post_list, 5) # Show 5 contacts per page

    # Make sure page request is an int. If not, deliver first page.
 	try:
		page = int(request.GET.get('page', '1'))
	except ValueError:
		page = 1

    # If page request (9999) is out of range, deliver last page of results.
	try:
		postlist = paginator.page(page)
	except (EmptyPage, InvalidPage):
		postlist = paginator.page(paginator.num_pages)
	
	return render_to_response('blog/post_list.html',{"postlist": postlist})
