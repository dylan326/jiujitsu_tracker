from django import forms


class NameForm(forms.Form):
    move_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    move_description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))