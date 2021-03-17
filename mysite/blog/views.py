from django.shortcuts import render, get_object_or_404

from .models import Post
# Create your views here.

def post_list(request):
    posts=Post.published.all()
    return render(request,'blog/post/post_list.html',{'posts':posts})

def post_detail(request,year,month,day,slug):
    post=get_object_or_404(Post,slug=slug,\
            status='published',\
            publish_year=year,\
            publish_month=month,\
            publish_day=day)

    return render(request,
                'blog/post/post_details.html',
                {'post':post}
                )