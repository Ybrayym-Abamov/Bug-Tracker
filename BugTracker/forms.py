from django import forms
from BugTracker.models import Ticket

#  REFERENCES:
#  https://simpleisbetterthancomplex.com/tutorial/2016/06/27/how-to-use-djangos-built-in-login-system.html


class LoginForm(forms.Form):
    username = forms.CharField(max_length=25, required=True)
    password = forms.CharField(max_length=100, required=True)
    email = forms.CharField(max_length=100, required=True)
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)


class TicketForm(forms.Form):
    title = forms.CharField(max_length=100, required=True)
    description = forms.CharField(widget=forms.Textarea, required=True)


class EditTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            'status',
            'description',
            'title',
            'assignedto'
        ]
