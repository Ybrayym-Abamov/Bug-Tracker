from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from BugTracker.forms import LoginForm, TicketForm
from BugTracker.models import Ticket, MyUser


#  REFERENCES:
#  https://docs.djangoproject.com/en/3.0/topics/auth/default/#how-to-log-a-user-in
#  https://docs.djangoproject.com/en/3.0/topics/auth/default/#redirecting-unauthorized-requests-in-class-based-views


@login_required
def main(request):
    #  TODO for later:
    #  Order it by ticket status
    data = Ticket.objects.all()
    return render(request, 'main.html', {"data": data})


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


@login_required
def ticketdetail(request, ticketid):
    ticketinfo = Ticket.objects.get(id=ticketid)
    return render(request, "ticket.html", {"ticketinfo": ticketinfo})


@login_required
def userinfo(request, userid):
    userinfo = MyUser.objects.all().filter(id=userid)
    return render(request, "userinfo.html", {"userinfo": userinfo})


@login_required
def createticket(request, filerid):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # getting the id of the ticket filer
            filer = MyUser.objects.get(id=filerid)
            Ticket.objects.create(
                title=data['title'],
                description=data['description'],
                usersubmited=filer
            )
            return HttpResponseRedirect(reverse('homepage'))
    Form = TicketForm()
    return render(request, 'form.html', {"Form": Form})


@login_required
def assignticket(request):
    pass


@login_required
def completedticket(request):
    pass


@login_required
def invalidticket(request):
    pass


@login_required
def editableticket(request):
    pass
