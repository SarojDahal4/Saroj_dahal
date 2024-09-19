from django.shortcuts import render, redirect
from .models import profession, contact
from .forms import  contactform, SignUpForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

# Create your views here.
def home (request):
    professions = profession.objects.all()
    context = {('professions'): professions}
    return render (request , "app/home.html", context)

def contact(request):
    if request.method == 'POST':
        form = contactform(request.POST)
        if form.is_valid():
            # Handle form submission, e.g., save data or send email
            form.save()  # or any other processing you want to do
            return redirect('contact')  # Redirect to a success page or elsewhere
    else:
        form = contactform()  # Initialize an empty form for GET request

    context = {'form': form}
    return render(request, 'app/contact.html', context)


def project (request): 
    context = {('project'): project}
    return render (request , "app/project.html", context)

def about (request):
    context = {('about'): about}
    return render (request , "app/about.html", context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Ensure that both username and password are provided
        if not username or not password:
            messages.error(request, "Both username and password are required.")
            return redirect('login')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in successfully.")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')

    else:
        return render(request, "app/login.html")
def logout_user (request): 
   logout(request)
   messages.success(request, "You have been logout....")
   return redirect ('home')



def register_user (request):
    form = SignUpForm()
    if request.method == "POST":
        form= SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate (username=username, password=password)
            login(request, user)
            messages.success(request, "You have register successfully.")
            return redirect ('home')
        else:
            messages.success(request, "Oops, Something went wrong..Please Try again")
            return redirect ('register')

    else:
        return render (request , "app/register.html", {'form':form})
    
def image (request): 
    return render (request , "app/image_i.html", {})

def Fimage (request): 
    return render (request , "app/image_fr.html", {})

def cv(request):
    return render (request, "app/cv.html",{})

def custom_404_view(request, exception):
    return redirect('home')