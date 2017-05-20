from django import forms
from .models import Diagnosis

class AddDiagnosisForm(forms.ModelForm):
	class Meta:
		model = Diagnosis
		fields = '__all__'
