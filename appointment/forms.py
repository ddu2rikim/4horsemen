from django import forms
from .models import Appointment

class AddAppointmentForm(forms.ModelForm):
	class Meta:
		model = Appointment
		fields = (
			'doctor_id',
			'user',
			'app_id'
		)

