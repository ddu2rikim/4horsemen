from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class Diagnosis(models.Model):
    diagnosis_id = models.AutoField(primary_key=True)
    exam_id = models.OneToOneField('examination.Examination', default="", null=False)
    app_id = models.OneToOneField('appointment.Appointment', default="", null=False)
    user = models.ForeignKey(User, default="", null=False)
    doctor_id = models.ForeignKey('doctor.Doctor', default="", null=False)
    icd10Code = models.ForeignKey('Icd10Code', default="", null=False)
    weight = models.CharField(max_length=200)
    temperature = models.CharField(max_length=200)
    blood_pressure = models.CharField(max_length=20)
    respiration = models.CharField(max_length=20)
    heart_rate = models.CharField(max_length=20)
    reflex = models.CharField(max_length=20)
    visual_activity = models.CharField(max_length=20)
    ears = models.CharField(max_length=20)
    skin_polar = models.CharField(max_length=20)
    lungs = models.CharField(max_length=20)
    throat = models.CharField(max_length=20)
    interview_note = models.TextField()
    confirm = models.CharField(max_length=1, default='N', null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fname

    def get_absolute_url(self):
        return reverse('diagnosis:diagnosis_list')


class Icd10Code(models.Model):
    icd10code = models.AutoField(primary_key=True)
    type = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return reverse('diagnosis:diagnosis_list')