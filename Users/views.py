from django.shortcuts import render, redirect
from Government.models import Location, Visitor
from .forms import ProfileForm, CustomUserCreationForm
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from datetime import date
from django.utils import timezone
import datetime
from django.contrib import messages

# Create your views here.


def Register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        profileForm = ProfileForm(request.POST)

        if form.is_valid() and profileForm.is_valid():
            user = form.save()

            profile = profileForm.save(commit=False)
            profile.user = user

            profile.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Account created successfully')
        return redirect('register')
    else:
        form = CustomUserCreationForm()
        profileForm = ProfileForm()
    
    return render(request, 'registration/register.html', {'form': form, 'profileform': profileForm})


@login_required
def DashBoard(request):
    today = date.today()

    visitor = Visitor.objects.filter(date_visited__year=today.year, date_visited__month=today.month, date_visited__day=today.day
                                                                        ).filter(staff=request.user).count()

    visitors = Visitor.objects.filter(status='Checked In').filter(date_visited__year=today.year, date_visited__month=today.month, date_visited__day=today.day
                                                                        ).filter(staff=request.user).count()

    visitorss = Visitor.objects.filter(status='Checked Out').filter(date_visited__year=today.year, date_visited__month=today.month, date_visited__day=today.day
                                                                        ).filter(staff=request.user).count()

    context = {
        'visitorsCount': visitor,
        'checkedIn': visitors,
        'checkedOut': visitorss
    }

    return render(request, 'registration/dashboard.html', context)

def Login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('dashboard')
    else:
        form = LoginForm()

    context = {
        'form': form
    }

    return render(request, 'registration/login.html', context)