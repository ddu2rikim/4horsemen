from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Patient
from .forms import AddPatientForm
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.utils import timezone



patient_list = ListView.as_view(model=Patient)

patient_detail = DetailView.as_view(model=Patient)

patient_new = CreateView.as_view(model=Patient, form_class=AddPatientForm)

patient_edit = UpdateView.as_view(model=Patient, form_class=AddPatientForm)

patient_delete = DeleteView.as_view(model=Patient, success_url=reverse_lazy('patient:patient_list'))
