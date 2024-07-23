from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# max length of 254 characters as an email address must not exceed that.

class SignUpForm(UserCreationForm):
 
    email = forms.EmailField(max_length=254, help_text='Please enter a valid email address.')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )


class TranslationForm(forms.Form):

    options = [
        ('en_to_es', 'English to Spanish'),
        ('es_to_en', 'Spanish to English'),
    ]
    text_to_translate = forms.CharField(widget=forms.Textarea, label = 'Enter text to translate')
    language_direction = forms.ChoiceField(choices=options, label = 'Translation Direction')