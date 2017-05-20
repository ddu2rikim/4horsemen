from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Appointment(models.Model):
	app_id = models.CharField(max_length=200)
	doctor_id = models.ForeignKey('doctor.Doctor', default="", null=False)
	user = models.ForeignKey(User, default="", null=False)


	def __str__(self):
		return self.app_id

	def get_absolute_url(self):
		return reverse('appointment:appointment_list')