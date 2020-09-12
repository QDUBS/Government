from django.shortcuts import render, redirect
from django.http import Http404
from .forms import VisitorRegForm
from .models import Location, Visitor
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from datetime import date
from django.utils import timezone
import datetime

from django.contrib import auth

from django.contrib import messages

# Create your views here.



@login_required
def VisRegPage(request):
    if request.method == 'POST':
        form = VisitorRegForm(request.POST)
        if form.is_valid():
            newvisitor = form.save(commit=False)
            newvisitor.staff = request.user
            newvisitor.save()

            #messages.success(request, 'Visitor added successfully')
            
        return redirect('allvisitors')
    else:
        form = VisitorRegForm()

    current_date = datetime.datetime.now()

    context = {
        'form': form,
        'current_date': current_date, 
    }
    
    return render(request, 'government/registration.html', context)


@login_required
def AllVisitorsPage(request):
    today = date.today()

    visitor = Visitor.objects.filter(date_visited__year=today.year, date_visited__month=today.month, date_visited__day=today.day
                                                                        ).filter(staff=request.user)

    context = {
        'visitors': visitor,
        'date': today
    }
    
    return render(request, 'government/allvisitors.html', context)


@login_required
def EditVisitorPage(request, visitor_id):

    visitor = Visitor.objects.get(id=visitor_id)

    if visitor.staff != request.user:
        raise Http404

    if request.method == 'POST':
        form = VisitorRegForm(instance=visitor, data=request.POST)

        if form.is_valid():
            form.save()
            #messages.success(request, 'Visitor info changed successfully')

        return redirect('allvisitors')
    else:
        form = VisitorRegForm(instance=visitor)

    context = {
        'form': form,
        'visitor': visitor,
    }
    
    return render(request, 'government/editvisitor.html', context)


@login_required
def Search(request):
    query = request.GET.get('query')

    if query != '' and query is not None:
        results = Visitor.objects.filter(Q(firstname__icontains=query) | 
                                         Q(lastname__icontains=query) |
                                         Q(middlename__icontains=query) |
                                         Q(state__icontains=query) |
                                         Q(tag_no__icontains=query) | 
                                         Q(location_visited__name__icontains=query) |
                                         Q(date_visited__icontains=query) |
                                         Q(status__icontains=query)
                                        ).filter(staff=request.user)
    else:
        raise Http404
    
    res = results

    context = {
        'results': res,
        'query': query
    }

    return render(request, 'government/search.html', context)


@login_required
def Status(request):
    today = date.today()
    
    visitors = Visitor.objects.filter(status='Checked In').filter(date_visited__year=today.year, date_visited__month=today.month, date_visited__day=today.day
                                                                        ).filter(staff=request.user)

    context = {
        'visitors': visitors
    }

    return render(request, 'government/status.html', context)

@login_required
def CheckedOut(request):
    today = date.today()
    
    visitors = Visitor.objects.filter(status='Checked Out').filter(date_visited__year=today.year, date_visited__month=today.month, date_visited__day=today.day
                                                                        ).filter(staff=request.user)

    context = {
        'visitors': visitors
    }

    return render(request, 'government/checkedout.html', context)