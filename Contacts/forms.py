from django import forms

COUNTRY = (
    'India', 'USA', 'UK', 'Australia',
)

GROUP = (
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
)


TYPE = (
    ('Consumer', 'Consumer'),
    ('Supplier', 'Supplier'),
)


class ContactForm(forms.Form):
    subject = forms.CharField()
    email = forms.EmailField(required=False)
    message = forms.CharField()


class ContactAddForm(forms.Form):
    Company_Name = forms.CharField(max_length=50)
    Primary_First_name = forms.CharField(max_length=50)
    Primary_Last_name = forms.CharField(max_length=50)
    Email = forms.EmailField()
    Contact_No = forms.CharField(max_length=20)
    Address = forms.CharField(max_length=250)
    Contact_Type = forms.ChoiceField(choices=TYPE)
    Contact_Group = forms.ChoiceField(choices=GROUP)