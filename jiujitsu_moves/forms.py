from django import forms
from .models import Moves

    
class AddMoveForm(forms.ModelForm):
    POSITION_CHOICES = [
        (1, 'Half Guard'),
        (2, 'Full Guard'),
        (3, 'Open/X Guard'),
        (4, 'Butterfly Guard'),
        (5, 'Worm Guard'),
        (6, 'Side Control'),
        (7, 'Mount'),
        (8, 'Back'),
    ]
    
    OFFENCE_DEFENSE = [
        (1, 'Offence'),
        (0, 'Defense'),
    ]
    
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}))
    position_id = forms.CharField(
        label='Select Position', widget=forms.Select(attrs={'class': 'form-control'}, choices=POSITION_CHOICES))
    is_offence = forms.CharField(
        label='Offence or Defense?', widget=forms.Select(attrs={'class': 'form-control'}, choices=OFFENCE_DEFENSE))
        
    class Meta:
        model = Moves
        fields = ['name', 'description', 'position_id', 'is_offence']

        

