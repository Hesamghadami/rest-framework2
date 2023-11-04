from django import forms
from .models import NewsLetter, ContactUs





class NewsLetterForm(forms.ModelForm):
    


    class Meta:
        model = NewsLetter
        fields = ['email']


class ContactUsForm(forms.ModelForm):
    


    class Meta:
        model = ContactUs
        fields = ['name', 'email','subject', 'message']



