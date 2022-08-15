from django.db import models

class Pro_Category(models.Model) :
    name=models.CharField(max_length=225)

    def __str__(self) :
        return self.name
    class Meta:
        verbose_name_plural='categories'


class Pro_Gallery(models.Model):
    image = models.ImageField(upload_to='portfolio/', default='./portfolio-1.jpg')

    class Meta:
        verbose_name_plural='gallery'

class Project(models.Model):
    pro_name=models.CharField(max_length=255)
    client=models.CharField(max_length=255)
    project_date=models.DateTimeField(null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey(Pro_Category, on_delete=models.DO_NOTHING,null=True, blank=True)
    gallery = models.ManyToManyField(Pro_Gallery)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    login_require = models.BooleanField(default=False)
    project_url=models.URLField(max_length=150)  
# Create your models here.
