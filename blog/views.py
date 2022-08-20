from django.db.models import Count
from django.db.models.functions import Now
from django.shortcuts import render
from blog.models import Post,Category,Comment
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from taggit.models import Tag
from django.shortcuts import redirect, render,get_object_or_404,HttpResponse,HttpResponseRedirect
from blog.forms import CommentForm
from django.contrib import messages

def blog_home_view(request,**kwargs):

    posts=Post.objects.filter(published_date__lte=Now(),status=1)
    tags=Tag.objects.all()
    categories = Category.objects.all().annotate(post_count= Count("courses"))

    if kwargs.get('cat_name') != None:
        posts=posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None :
        posts=posts.filter(author__username=kwargs['author_username'])
    if kwargs.get('tag_name') != None :
        posts=posts.filter(tags__name__in=[kwargs['tag_name']]) #kwargs should be in brackets!!__in means is it exists init?
    
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



def blog_single_view(request,**kwargs):

    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            form.save()
            
            messages.add_message(request,messages.SUCCESS,'your comment submited successfully')
        else:
            messages.add_message(request,messages.ERROR,'your comment did not submited')

    form= CommentForm()

    posts=Post.objects.filter(published_date__lte=Now(),status=1)
    tags=Tag.objects.all()
    categories = Category.objects.all().annotate(post_count= Count("courses"))

    if kwargs.get('pid') != None:
        post=get_object_or_404(Post, pk=kwargs['pid'],published_date__lte =Now(),status=1)
        comments=Comment.objects.filter(post=post.id,approach=True)

        def counter ():
            post.counted_views +=1
            post.save()
        counter()
        
    context={'posts':posts,'tags':tags,'categories':categories,'post':post,'form':form,'comments':comments }
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
