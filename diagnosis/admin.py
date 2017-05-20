from django.contrib import admin
from .models import Diagnosis

@admin.register(Diagnosis)
class DiagnosisAdmin(admin.ModelAdmin):
	list_display = ('app_id','exam_id','user','doctor_id','icd10Code')

