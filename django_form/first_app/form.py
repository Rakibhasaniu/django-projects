from django import forms


class contact_form(forms.Form):
    name = forms.CharField(label='User Name')
    file = forms.FileField()
    # email = forms.EmailField()
    # age=forms.IntegerField()
    # weight= forms.FloatField()
    # balance=forms.DecimalField()
    # check = forms.BooleanField()
    # CHOICE= [('S','SMALL'),('M','MEDIUM'),('L','LARGE')]
    # size= forms.ChoiceField(choices=CHOICE)
    # MEAL=[('V','VAT'),('M','MANGSHO'),('D','DAL')]
    # khabar= forms.MultipleChoiceField(choices=MEAL)