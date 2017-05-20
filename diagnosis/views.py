from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Diagnosis
from .forms import AddDiagnosisForm
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy



diagnosis_list = ListView.as_view(model=Diagnosis)

diagnosis_detail = DetailView.as_view(model=Diagnosis)

diagnosis_new = CreateView.as_view(model=Diagnosis, form_class=AddDiagnosisForm)

diagnosis_edit = UpdateView.as_view(model=Diagnosis, form_class=AddDiagnosisForm)

diagnosis_delete = DeleteView.as_view(model=Diagnosis, success_url=reverse_lazy('diagnosis:diagnosis_list'))

diagnosis_transfer = CreateView.as_view(model = Diagnosis, form_class=AddDiagnosisForm)