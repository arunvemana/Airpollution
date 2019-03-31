from django import forms


class UserInputData(forms.Form):
    no2 = forms.IntegerField()
    co2 = forms.IntegerField()
    zn = forms.IntegerField()
    h = forms.IntegerField()
