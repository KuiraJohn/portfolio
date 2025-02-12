from django import forms
from cv.models import contactme


class contactmeForm(forms.ModelForm):
    class Meta:
        model=contactme
        fields= ['name', 'email', 'subject', 'message', 'phone_number']