from django import forms

class UserForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
    languages = forms.ChoiceField(choices=((1, "English"), (2, "German"), (3, "French")))
    password = forms.CharField(widget= forms.PasswordInput)
