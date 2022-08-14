from django.db.models import Count
from django.db.models.functions import Now
from django.shortcuts import render
from blog.models import Post,Category,Comment
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from taggit.models import Tag

def blog_home_view(request):

    posts=Post.objects.filter(published_date__lte=Now(),status=1)
    tags=Tag.objects.all()
    categories = Category.objects.all().annotate(post_count= Count("courses"))
    
    posts=Paginator(posts,3)
    page_number=request.GET.get('page')

    try :
        posts=posts.get_page(page_number)
    except PageNotAnInteger:
        posts=posts.get_page(1)
    except EmptyPage:
        posts=posts.get_page(1)


    context={'posts':posts,'tags':tags,'categories':categories }
    return render(request,'blog/blog.html',context)



def blog_single_view(request):
    posts=Post.objects.filter(published_date__lte=Now(),status=1)
    tags=Tag.objects.all()
    categories = Category.objects.all().annotate(post_count= Count("courses"))

    context={'posts':posts,'tags':tags,'categories':categories }
    return render(request,'blog/blog-single.html',context)


def blog_search(request):
    posts=Post.objects.filter(published_date__lte =Now(),status=1)
    if request.method == 'GET':
        #print(request.GET.get('s'))
        #if (x := request.GET.get('s')) : #warlus operator :=
            posts=posts.filter(content__contains=request.GET.get('s'))
    context={'posts':posts }
    return render(request,'blog/blog.html',context)

# Create your views here.
