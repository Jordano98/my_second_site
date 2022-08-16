from django import template
from blog.models import Post
register= template.Library()


@register.inclusion_tag('website/recent-post.html')
def recent_posts ():
    posts=Post.objects.filter(status=1).order_by('-published_date')[:4]
    return {'posts':posts}