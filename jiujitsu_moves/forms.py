from django import forms
from .models import Moves

    
class AddMoveForm(forms.ModelForm):
    POSITION_CHOICES = [
        (1, 'Half Guard'),
        (2, 'Full Guard'),
    ]
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}))
    position_id = forms.CharField(
        label='Select Position', widget=forms.Select(attrs={'class': 'form-control'}, choices=POSITION_CHOICES))
        
    class Meta:
        model = Moves
        fields = ['name', 'description', 'position_id']

        

