from django import forms
from .models import Examination

class AddExaminationForm(forms.ModelForm):
	class Meta:
		model = Examination
		fields = '__all__'

