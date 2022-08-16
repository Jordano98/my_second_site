from django import template
from blog.models import Post,Category,Comment
register= template.Library()

@register.simple_tag(name='comment_count')
def function(pid):
    return Comment.objects.filter(post=pid,approach=1).count()

@register.filter
def snippet(value,arg=20):
    return value[:arg]+'...'

@register.inclusion_tag('blog/recent-posts.html')
def recent_posts ():
    posts=Post.objects.filter(status=1).order_by('-published_date')[:4]
    return {'posts':posts}