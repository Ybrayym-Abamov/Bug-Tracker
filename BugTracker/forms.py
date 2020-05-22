from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=25)
    password = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)


class TicketForm(forms.Form):
    pass
