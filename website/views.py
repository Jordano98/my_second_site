from django.shortcuts import render


def index_view(request):
    return render(request,'website/index.html')


def contact_view(request):
    return render(request,'website/contact.html')


def team_view(request):
    return render(request,'website/team.html')

# Create your views here.
