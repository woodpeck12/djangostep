#mysite\mysite\forms.py

from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(required=False, label = 'Your email is')
    message = forms.CharField(widget=forms.Textarea)

#woodpeck - this is validation check of form value.
#method name must be clean_ field name as below:
    def clean_message(self):   
    	message = self.cleaned_data['message']
    	num_words = len(message.split())
    	if num_words < 7:
    		raise forms.ValidationError('need to do put more than 7 words')
    	return message