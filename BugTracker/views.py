from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from BugTracker.forms import LoginForm, TicketForm, EditTicketForm
from BugTracker.models import Ticket, MyUser


#  REFERENCES:
#  https://docs.djangoproject.com/en/3.0/topics/auth/default/#how-to-log-a-user-in
#  https://docs.djangoproject.com/en/3.0/topics/auth/default/#redirecting-unauthorized-requests-in-class-based-views


@login_required
def main(request):
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
    return HttpResponseRedirect(reverse('login'))


@login_required
def ticketdetail(request, ticketid):
    ticketinfo = Ticket.objects.get(id=ticketid)
    return render(request, "ticket.html", {"ticketinfo": ticketinfo})


@login_required
def userinfo(request, filerid):
    filer = MyUser.objects.get(id=filerid)
    filerhistory = Ticket.objects.filter(ticketfiler=filer)
    assigned = filerhistory.filter(status="InP")
    completed = filerhistory.filter(status="D")
    reported = filerhistory.filter(status="N")
    return render(request, 'userinfo.html', {'filerhistory': filerhistory,
                  'filer': filer, 'assigned': assigned, 'completed': completed,
                                             'reported': reported})


@login_required
def createticket(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            filer = request.user
            Ticket.objects.create(
                title=data['title'],
                description=data['description'],
                ticketfiler=filer
            )
            return HttpResponseRedirect(reverse('homepage'))
    form = TicketForm()
    return render(request, 'form.html', {"form": form})


@login_required
def assignticket(request, userid, ticketid):
    user = MyUser.objects.get(id=userid)
    data = Ticket.objects.get(id=ticketid)
    data.assignedticket = user
    data.status = "InP"
    data.save()
    return HttpResponseRedirect(reverse('ticketdetail', args=(ticketid, )))


@login_required
def completedticket(request, userid, ticketid):
    user = MyUser.objects.get(id=userid)
    data = Ticket.objects.get(id=ticketid)
    data.doneticket = user
    data.status = "D"
    data.save()
    return HttpResponseRedirect(reverse('ticketdetail', args=(ticketid, )))


@login_required
def invalidticket(request, userid, ticketid):
    user = MyUser.objects.get(id=userid)
    data = Ticket.objects.get(id=ticketid)
    data.invalidticket = user
    data.status = "InV"
    data.save()
    return HttpResponseRedirect(reverse('ticketdetail', args=(ticketid, )))


@login_required
def editticket(request, ticketid):
    ticket = Ticket.objects.get(id=ticketid)
    if request.method == "POST":
        form = EditTicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            ticket.title = data['title']
            ticket.description = data['description']
            # ticket.status = data['status'],
            # ticket.assignedto = data['assignedto']
            ticket.save()
            return HttpResponseRedirect(reverse('ticketdetail', args=(ticketid, )))
    form = EditTicketForm(initial={
        'title': ticket.title,
        'description': ticket.description,
        # 'status': ticket.status,
        # 'assignedto': ticket.assignedto,
    })
    return render(request, 'form.html', {"form": form})
