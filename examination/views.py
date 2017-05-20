from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Examination
from .forms import AddExaminationForm
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy

#for Transfer result of examination

from diagnosis.models import Diagnosis
from diagnosis.forms import AddDiagnosisForm

examination_list = ListView.as_view(model = Examination)

examination_detail = DetailView.as_view(model = Examination)

examination_new = CreateView.as_view(model = Examination, form_class=AddExaminationForm)

examination_edit = UpdateView.as_view(model = Examination, form_class=AddExaminationForm)

examination_delete = DeleteView.as_view(model = Examination, success_url=reverse_lazy('examination:examination_list'))

examination_transfer = CreateView.as_view(model = Examination, form_class=AddExaminationForm)