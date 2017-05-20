from django.contrib import admin
from .models import Examination

@admin.register(Examination)
class ExaminationAdmin(admin.ModelAdmin):
	list_display = ('exam_id','app_id','user','doctor_id')