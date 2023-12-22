from django import forms

class CustomForm(forms.Form):
    username=forms.CharField(label='username')
    password=forms.CharField(label='password',widget=forms.PasswordInput)
