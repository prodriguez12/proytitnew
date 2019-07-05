from django import forms

from .models import Input

class InputForm(forms.ModelForm):
	class Meta:
		model = Input
		fields =['red_vial_layer', 'GPS_layer', 'gbd',  'description', 'metrica']