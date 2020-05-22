from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from BugTracker.forms import LoginForm, TicketForm
from BugTracker.models import Ticket, MyUser


def main(request):
    return render(request, 'main.html')


def login_request(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request,
                username=data['username'],
                password=data['password'],
                email=data['email'],
                first_name=data['first_name'],
                last_name=data['last_name']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('homepage'))
            else:
                messages.error(request, "Invalid credentials")
                return HttpResponseRedirect(reverse('login'))
    else:
        form = LoginForm()
    return render(request, 'form.html', {"form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return HttpResponseRedirect(reverse('homepage'))
