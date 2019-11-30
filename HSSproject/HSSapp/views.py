from django import forms
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from django.views import View
# Create your views here.
from django.views.generic import CreateView
from .forms import newuserform, login, profileform,locationform
from .models import User, RequestWork, JobCategory, Profile, Area, Feedback, Notification,Location


def Register(request):
    if request.method == "GET":
        form = newuserform()
    if request.method == "POST":
        form = newuserform(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print("Success")
            # return index(request)
            return redirect('login')
        else:
            print('error from invalid')
    return render(request, 'HSSapp/registration.html', {'form': form})


def loginview(request):
    if request.method == 'GET':
        form = login()
        print("inside get")
        return render(request, 'HSSapp/login.html', {'form': form})
    if request.method == 'POST':
        form = login(request.POST)
        print('inside post')
        if form.is_valid():
            print("form is valid")
            # form.save(commit=True)

            name = form.cleaned_data['username']
            pwd = form.cleaned_data['password']

            print(name, pwd)
            print("login successfull")
            request.session['user'] = name
            return render(request, 'HSSapp/mypage.html', {'form': form, 'user': name})

    return render(request, 'home.html')


def logoutview(request):
    request.session['user'] = None
    return loginview(request)


def profilecreate(request):
    if request.method == 'GET':
        form = profileform()
        return render(request, 'HSSapp/profile.html', {'form': form})
    if request.method == 'POST':
        form = profileform(request.POST)
        if form.is_valid():
            print('inside post')
            u = User.objects.get(username=request.session['user'])
            fname = form.cleaned_data['firstname']
            lname = form.cleaned_data['lastname']
            phone = form.cleaned_data['phone']
            job = form.cleaned_data['job']
            p = Profile(name=u, firstname=fname, lastname=lname, phone=phone, job=job)
            p.save()
            return render(request, 'HSSapp/mypage.html')
        return render(request, 'HSSapp/profile.html', {'form': form})
    return render(request, 'mypage.html')

def locationcreate(request):
    if request.method == 'GET':
        form = locationform()
        print('inside location get')
        return render(request, 'HSSapp/location.html', {'form': form})
    if request.method == 'POST':
        form = locationform(request.POST)
        if form.is_valid():
            print('inside post')
            u = User.objects.get(username=request.session['user'])
            state = form.cleaned_data['state']
            district = form.cleaned_data['district']
            area = form.cleaned_data['area']
            place = form.cleaned_data['place']
            p = Location(name=u, state=state, district=district, area=area, place=place)
            p.save()
            return render(request, 'HSSapp/mypage.html')
        return render(request, 'HSSapp/location.html', {'form': form})
    return render(request, 'mypage.html')