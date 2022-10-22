from django import forms




class Proccess1CFileForm(forms.Form):
    CHOICES = [('All','All'),('Admin','Admin'), ('Teacher','Teacher')]

    type = forms.RadioSelect(choices=CHOICES)
    file = forms.FileInput()

f = Proccess1CFileForm()
print(f.as_p)