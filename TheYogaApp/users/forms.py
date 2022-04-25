from django import forms

from problems.models import Problems


class UserRegistrationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    emailId = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    f_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    l_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    height = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Height in cm'}))
    weight = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Weight in kg'}))
    dob = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'Date of Birth', 'type': 'date'}))
    medical_conditions = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                                        queryset=Problems.objects.all())


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
