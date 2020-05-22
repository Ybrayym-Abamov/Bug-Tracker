from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=25, required=True)
    password = forms.CharField(max_length=100, required=True)
    email = forms.CharField(max_length=100, required=True)
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)


class TicketForm(forms.Form):
    pass
