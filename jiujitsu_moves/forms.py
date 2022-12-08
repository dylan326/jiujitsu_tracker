from django import forms
from .models import Moves, Positions
from django.forms import ModelChoiceField

class PositionsModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s" % obj.position_name
    
class AddMoveForm(forms.ModelForm):
    
    OFFENCE_DEFENSE = [
        (1, 'Offence'),
        (0, 'Defense'),
    ]
    
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}))
    position = PositionsModelChoiceField(label='Position',widget=forms.Select(attrs={'class': 'form-control'}),queryset=Positions.objects.all(),initial = Positions.objects.get(id=1))
    is_offence = forms.CharField(
        label='Offence or Defense?', widget=forms.Select(attrs={'class': 'form-control'}, choices=OFFENCE_DEFENSE))
        
    class Meta:
        model = Moves
        fields = ['name', 'description', 'position', 'is_offence']

        

