from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    # password2 = forms.CharField(label = 'password2', required=False)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']