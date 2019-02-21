# MIT License

# Copyright (c) Justin James Gonzales, Thomas Martin Saliba, Brent Zaguirre

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


# “This is a course requirement for CS 192 Software Engineering II under the supervision of 
# Asst. Prof. Ma. Rowena C. Solamo of the Department of Computer Science, College of Engineering, 
# University of the Philippines, Diliman for the AY 2015-2016”.
# =================================================================================   

# Creation Date: <1/26/2019>

# =================================================================================

# Development Group: What's Your IGP

# =================================================================================

# Client Group: What's Your IGP

# =================================================================================

# Purpose:
# > The purpose of the project: "What's Your IGP," is for the fufillment of the course: "CS 192." The project
# aims to centralize the Income Generated Projects (IGP's) online information of all existing organizations
# associated with UP Diliman. It's objective is to offer convenience for both sellers and customers of IGP
# to sell and gather information online.  

# =================================================================================

from . import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
CHOICES=[('select1','Seller'),
         ('select2','Buyer')]

class SignUpForm(UserCreationForm):
    user_type = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    college = forms.CharField(max_length=30, required=True, help_text='Required.')
    #first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    #last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    #email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    mobile_number = forms.CharField(required=True, label="Contact no", widget=forms.TextInput(
        attrs={'class': 'form-control form-group',
               'placeholder': '+639999999999'})
        )
    class Meta:
        model = User
        fields = ('username','mobile_number','user_type','college', 'password1', 'password2' )

class Orgform(forms.ModelForm):
    org_name = forms.CharField(required=True, label="Organization", widget=forms.TextInput)
    location = forms.CharField(required=True, label="Location", widget=forms.TextInput)
    class Meta:
      model=User
      fields=('org_name','location')

class LoginForm(AuthenticationForm):
    username = forms.CharField(required=True, label="Username", widget=forms.TextInput(
        attrs={'class': 'form-control form-group',
               'placeholder': 'username'})
        )
    password = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={'class': 'form-control form-group',
               'name': 'password',
               'id': 'password',
               'placeholder': 'password'})
        )
    class Meta:
        fields = ('username', 'password')    

class RegistrationForm(UserCreationForm):
    username = forms.CharField(required=True, label="Username", widget=forms.TextInput(
        attrs={'class': 'form-control form-group',
               'placeholder': 'username'})
        )

    email = forms.EmailField(required=True, label="Email", widget=forms.TextInput(
        attrs={'class': 'form-control form-group',
               'placeholder': 'email'})
        )

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={'class': 'form-control form-group',
               'name': 'password',
               'id': 'password',
               'placeholder': 'Enter your password'})
        )

    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput(
        attrs={'class': 'form-control form-group',
               'name': 'password',
               'id': 'password',
               'placeholder': 'Confirm password'})
        )

    first_name = forms.CharField(required=True, label="First name", widget=forms.TextInput(
        attrs={'class': 'form-control form-group',
               'placeholder': 'first name'})
        )

    last_name = forms.CharField(required=True, label="Last name", widget=forms.TextInput(
        attrs={'class': 'form-control form-group',
               'placeholder': 'last name'})
        )
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if (commit):
            user.save()

        return user


# After registering, satisfying default fields in built-in User model
# Create User Profile consisting of contact no. and date of birth
class CreateUserProfile(forms.ModelForm):
    date_of_birth = forms.CharField(label="Date of birth", widget=forms.TextInput(
        attrs={'class': 'form-control form-group',
               'placeholder': 'YYYY-MM-DD',
               'type': 'date',
               'required pattern': '[0-9]{4}-[0-9]{2}-[0-9]{2}'})
        )

    phone_number = forms.CharField(required=True, label="Contact no", widget=forms.TextInput(
        attrs={'class': 'form-control form-group',
               'placeholder': '+639999999999'})
        )
    class Meta:
        model = models.UserProfile
        fields = ('date_of_birth', 'phone_number')
        exclude = ('user',)
class EditContactInfoForm(forms.Form):
    email = forms.EmailField(required=True, label="Email", widget=forms.TextInput(
        attrs={'class': 'form-control form-group',
               'placeholder': 'Email'})
        )

    phone_number = forms.CharField(required=True, label="Contact no", widget=forms.TextInput(
        attrs={'class': 'form-control form-group',
               'placeholder': '+639999999999'})
        )
