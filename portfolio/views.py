from django.shortcuts import render
from portfolio.models import Project,Pro_Gallery,Pro_Category
from django.shortcuts import redirect, render,get_object_or_404


def portfolio_view(request):
    projects=Project.objects.all()

    context={'projects':projects}
    return render(request,'portfolio/portfolio.html',context)


def portfolio_details_view(request,pid):
    project=get_object_or_404(Project, pk=pid)

    context={'project':project}
    return render(request,'portfolio/portfolio-details.html',context)

# Create your views here.
