from django import forms

GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)


class DetailForm(forms.Form):
    Gender = forms.ChoiceField(GENDER)
    Contact_no = forms.CharField(max_length=12)
    Company_name = forms.CharField(max_length=50)
    DOB = forms.DateField(label='Date of Birth (MM/DD/YY)')
    Address = forms.CharField(max_length=250)