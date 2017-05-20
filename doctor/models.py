from django.db import models
from django.core.urlresolvers import reverse

class Doctor(models.Model):
	doctor_id = models.AutoField(primary_key=True)
	fname = models.CharField(max_length=200)
	mname = models.CharField(max_length=200)
	lname = models.CharField(max_length=200)
	dob = models.DateTimeField(auto_now_add=False)
	sex = models.CharField(max_length=20)
	addr1 = models.CharField(max_length=20)
	addr2 = models.CharField(max_length=20)
	addr3 = models.CharField(max_length=20)
	city = models.CharField(max_length=20)
	county = models.CharField(max_length=20)
	state = models.CharField(max_length=20)
	country = models.CharField(max_length=20)
	zipcode = models.CharField(max_length=20)
	phone1 = models.CharField(max_length=20)
	phone2 = models.CharField(max_length=20)
	phone3 = models.CharField(max_length=20)
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.fname

	def get_absolute_url(self):
		return reverse('doctor:doctor_list')