
from django import forms
from django.contrib.auth.models import User
from .models import User
from django.forms import ModelForm, TextInput, EmailInput
 
class profileform(forms.ModelForm):
    class Meta:
        model=User
        fields=[   'first_name',   'last_name',   'date_of_birth',   'username',   'email',   'state','district','pincode',   'phone_number',   'bio',   'profile_pic'  ]

        widgets = {   'first_name': TextInput(attrs={    'class': "form-control",    'style': 'max-width: 300px;',    'placeholder': 'First Name'    }),  'last_name': TextInput(attrs={    'class': "form-control",    'style': 'max-width: 300px;',    'placeholder': 'Last Name'    }),  'date_of_birth': TextInput(attrs={    'class': "form-control",    'style': 'max-width: 300px;',    'placeholder': 'Date of Birth'    }),  'username': TextInput(attrs={    'class': "form-control",    'style': 'max-width: 300px;',    'placeholder': 'Username'    }),   'email': EmailInput(attrs={    'class': "form-control",    'style': 'max-width: 300px;',    'placeholder': 'Email'    }),  'state': TextInput(attrs={    'class': "form-control",    'style': 'max-width: 300px;',    'placeholder': 'state' }),  'district': TextInput(attrs={    'class': "form-control",    'style': 'max-width: 300px;',    'placeholder': 'district' }),  'pincode': TextInput(attrs={    'class': "form-control",    'style': 'max-width: 300px;',    'placeholder': 'pincode' }), 'phone_number': TextInput(attrs={ 'class': "form-control", 'style': 'max-width: 300px;', 'placeholder': 'Mobile Number' }), 'bio': TextInput(attrs={ 'class': "form-control", 'style': 'max-width: 300px;', 'placeholder': 'Bio' }), }

