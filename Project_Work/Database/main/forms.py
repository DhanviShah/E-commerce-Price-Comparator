from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm ,PasswordChangeForm
class UserSignUpForm(UserCreationForm):
    email=forms.EmailField(max_length=70)
    class Meta:
        model=User
        fields=('username','email','password1','password2')

class Search(forms.Form):
    name=forms.CharField(widget =forms.TextInput(attrs={'placeholder': 'Search', 'class': 'form-control'}))

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password']

