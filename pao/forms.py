from django import forms
from django.core.validators import FileExtensionValidator

CHOICES = [('Admin','АУП'), ('Teacher','ППС'),('All','Все')]

class Proccess1CFileForm(forms.Form):
    
    types = forms.ChoiceField(widget=forms.RadioSelect(attrs = {"class":"form-check-input",
     "type":"radio", "name":"flexRadioDefault"}), choices = CHOICES, )
    file = forms.FileField(widget=forms.FileInput(attrs = {"class":"form-control", "type":"file", 
    "id":"formFile", "onchange":"deleteWarning()", 'accept': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/vnd.ms-excel'}),
    validators=[FileExtensionValidator(allowed_extensions=["xlsx"])])
