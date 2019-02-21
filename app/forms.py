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
