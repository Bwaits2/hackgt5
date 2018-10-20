from django import forms

class FilterForm(forms.Form):
    include_democrat = forms.BooleanField(required=False)
    include_republican = forms.BooleanField(required=False)
    include_neutral = forms.BooleanField(required=False)
