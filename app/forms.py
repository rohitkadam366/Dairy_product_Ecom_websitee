from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordResetForm
from django.contrib.auth.models import User
from . models import Customer,STATE_CHOICES
from django_select2.forms import Select2Widget

class CustomerLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', max_length=30, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super(CustomerLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Custom Username Label"
        self.fields['password'].label = "Custom Password Label"

class CustomerRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus':'True','class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))


    class meta:
        model = User
        fields= ['username','email','password1','password2']


class mypasswordresetform(PasswordResetForm):
    email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'class':'form-control'}))



class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'locality', 'city', 'state', 'zipcode']
        widgets = {
            'state': Select2Widget(attrs={'class': 'form-control'}),
        }

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    locality = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    state = forms.ChoiceField(choices=STATE_CHOICES, widget=Select2Widget(attrs={'class': 'form-control'}))
    zipcode = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    



