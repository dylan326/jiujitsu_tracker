from django import forms

POSITION_CHOICES = [
    (1, 'Half Guard'),
    (2, 'Full Guard'),
]

    
class NameForm(forms.Form):
    move_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    move_description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}))
    move_position = forms.CharField(
        label='Select Position', widget=forms.Select(attrs={'class': 'form-control'}, choices=POSITION_CHOICES))

