from django import forms
from aerodrome.models.aerodrome import Aerodrome


class AerodromeAdminForm(forms.ModelForm):
    icao_code = forms.CharField(label='ICAO code', max_length=4)
    name = forms.CharField(label='Name')
    city = forms.CharField(label='City')

    class Meta:
        model = Aerodrome
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'style': 'width: 100%; max-width: 300px;'}),
            'city': forms.TextInput(attrs={'style': 'width: 100%; max-width: 300px;'}),
        }
