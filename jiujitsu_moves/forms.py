from django import forms


class NameForm(forms.Form):
    move_name = forms.CharField(label='Your name', max_length=100)
    move_description = forms.CharField(widget=forms.Textarea)