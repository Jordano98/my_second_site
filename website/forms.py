from django import forms
from website.models import Newsletter,Contact

class Newsletterform(forms.ModelForm):

    class Meta :
        model=Newsletter
        fields= '__all__'

class Contactform(forms.ModelForm):

    class Meta:
        model=Contact
        fields= '__all__'