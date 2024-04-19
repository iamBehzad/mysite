from django import forms
from website.models import Contact,Newsletter

class ContactForm(forms.ModelForm):
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name:
            name = 'ناشناس'
        return name

    class Meta:
        model = Contact
        fields = '__all__'
        
class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'