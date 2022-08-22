from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordResetForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("/")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="accounts/register.html", context={"form":form})

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form=AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                username=form.cleaned_data.get('username')
                password=form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request,user)
                    return redirect('/')
        form=AuthenticationForm()#this is really neccessary item for rendring template completely fine
        context={'form':form}
        return render (request,'accounts/login.html',context)
    else:
        return redirect('/')

@login_required(login_url='/accounts/login')
def logout_view(request):
    #if request.user.is_authenticated:
    logout(request)
    return redirect('/')
