from django.shortcuts import render
from website.forms import Newsletterform,Contactform
from django.contrib import messages
from django.shortcuts import redirect, render,get_object_or_404,HttpResponse,HttpResponseRedirect
from website.models import Team

def index_view(request):
    return render(request,'website/index.html')


def contact_view(request):
    if request.method=='POST':
        form=Contactform(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your TICKET submited successfully')
        else:
            messages.add_message(request,messages.ERROR,'your TICKET did not submited')
            
    form=Contactform()
    return render(request,"website/contact.html",{'form':form})


def team_view(request):
    pass
    members=Team.objects.all()

    context={'members':members}
    return render(request,'website/team.html',context)

def newsletter_view(request):
    if request.method=='POST':
        form=Newsletterform(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your email submited successfully')
        else:
            messages.add_message(request,messages.ERROR,'your email did not submited')
        return HttpResponseRedirect('./')
    form=Newsletterform()
# Create your views here.
