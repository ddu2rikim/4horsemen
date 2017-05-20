from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Doctor
from .forms import AddDoctorForm
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy



doctor_list = ListView.as_view(model=Doctor)

doctor_detail = DetailView.as_view(model=Doctor)

doctor_new = CreateView.as_view(model=Doctor, form_class=AddDoctorForm)

doctor_edit = UpdateView.as_view(model=Doctor, form_class=AddDoctorForm)

doctor_delete = DeleteView.as_view(model=Doctor, success_url=reverse_lazy('doctor:doctor_list'))