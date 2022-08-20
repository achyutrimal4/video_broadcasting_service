from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from users.forms import RegistrationForm, UsersAuthenticationForm, ProfileUpdateForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings
from .models import Profile
from django.contrib.auth.decorators import login_required, user_passes_test
from verify_email.email_handler import send_verification_email

# Create your views here.


def register_view(request):
    
    user = request.user
    if user.is_authenticated:
        return redirect('home')
    
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            
            # email = form.cleaned_data.get('email')
            # raw_password = form.cleaned_data.get('password')
            # # user = authenticate (email=email, password=raw_password)
            # inactive_user = send_verification_email(request, form)
            user = form.save(commit=False)
            user.is_active=True
            user.save()

            messages.info(
                request, 'Account created. Please check your inbox and verify your email to continue.')
            return redirect('login')
        else:
            context['registration_form'] = form
    else:  # GET request
        form = RegistrationForm()
        context['registration_form'] = form

    return render(request, 'users/register.html', context)


def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        if user.is_superuser:
            return redirect('admin_panel')
        else:
            return redirect('home')

    if request.method == "POST":
        form = UsersAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(request, email=email, password=password)
            if user: 
                login(request, user)
                if user.is_superuser:
                    return redirect('admin_panel')
                else:
                    return redirect('home')
                
    else:
        form = UsersAuthenticationForm()

    context['login_form'] = form
    return render(request, 'users/login.html', context)


def logout_view(request):
    logout(request)
    # messages.success(request, 'User was successfully logged out.')
    return redirect('landing_page')

@login_required(login_url ='login')
def profile_view(request, pk):
    user_profile = Profile.objects.get(id=pk)
    context = {'user_profile': user_profile}
    return render(request, 'users/users_profile.html', context)

@login_required(login_url ='login')
def edit_profile(request, pk):
    profile = request.user.profile
    form=ProfileUpdateForm(instance=profile)
    
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('myprofile')
    context={'form':form}
    return render(request, 'users/editProfile.html', context)