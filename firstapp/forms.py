from django import forms
from firstapp.models import studentmodel

def namevalidator(value):
    if len(value)<4:
        raise forms.ValidationError("Name len should be greater than 4")
def emailvalidator(value):
    if value.split("@")[1]!="gmail.com":
        raise forms.ValidationError("Mail should be gmail only")

class studentform(forms.ModelForm):
    name=forms.CharField(validators=[namevalidator])
    email=forms.EmailField(validators=[emailvalidator])
    class Meta:
        model=studentmodel
        fields="__all__"
