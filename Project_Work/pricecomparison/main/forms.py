from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm ,PasswordChangeForm
class UserSignUpForm(UserCreationForm):
    username=forms.CharField(widget =forms.TextInput(attrs={'placeholder': 'Username','class':'box'}))
    email=forms.CharField(widget= forms.EmailInput(attrs={'placeholder':'Email','class':'box'}))
    password1=forms.CharField(widget =forms.PasswordInput(attrs={'placeholder': 'Password','class':'box'}))
    password2=forms.CharField(widget =forms.PasswordInput(attrs={'placeholder': 'Re-Enter Password','class':'box'}))
    class Meta:
        model=User
        fields=('username','email','password1','password2')

class Search(forms.Form):
    name=forms.CharField(widget =forms.TextInput(attrs={'placeholder': 'Search', 'class': 'form-control'}))

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password']

# class PasswordChangeForm(SetPasswordForm):
#     old_password=forms.CharField(widget =forms.PasswordInput(attrs={'placeholder': 'Old Password'}))
#     new_password=forms.CharField(widget =forms.PasswordInput(attrs={'placeholder': 'New Password'}))
#     reenter_new_password=forms.CharField(widget =forms.PasswordInput(attrs={'placeholder': 'Re-Enter New Password'}))
#     class Meta:
#         model=User
#         field=('old_password','new_password','reenter_new_password')

