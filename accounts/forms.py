from django import forms
from .models import CustomUser


class UserAdd(forms.ModelForm):
    model = CustomUser
    fields = ('email','username', 'first_name', 'last_name')