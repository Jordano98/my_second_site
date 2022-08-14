from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# Create your models here.
class Category(models.Model) :
    name=models.CharField(max_length=225)

    def __str__(self) :
        return self.name
    class Meta:
        verbose_name_plural='categories'

class Post(models.Model):
    image = models.ImageField(upload_to='blog/', default='./blog-1.jpg')
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True) 
    title = models.CharField(max_length=255)
    content = models.TextField()
    tags = TaggableManager() 
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name="courses",null=True, blank=True)
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    login_require = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering=['-created_date']
    def __str__(self) :
        return '{}-{}'.format(self.title,self.id)


class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE ,null=True)
    name=models.CharField(max_length=255)
    email=models.EmailField()
    subject=models.CharField(max_length=255)
    massage=models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    approach=models.BooleanField(default=False)

    class Meta:
        ordering=['-created_date']
    def __str__(self) :
        return '{}'.format(self.name)

# Create your models here.
