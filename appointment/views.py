from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Appointment
from .forms import AddAppointmentForm
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import (authenticate, login, get_user_model, logout,)
from django.views.generic import View



#appointment_list = ListView.as_view(model=Appointment)

appointment_list = ListView.as_view(queryset=Appointment.objects.order_by('app_id')[:10],
               context_object_name='appointment_list',
               template_name='appointment/appointment_list.html')


'''

def appointment_list(request):
    print(request.user) #test13
    print(request.user.id)  # test13
    args = {'user': request.user}
    #print(args)
    return render(request, 'appointment/appointment_list.html', args)

'''
appointment_detail = DetailView.as_view(model=Appointment)

appointment_new = CreateView.as_view(model=Appointment, form_class=AddAppointmentForm)

appointment_edit = UpdateView.as_view(model=Appointment, form_class=AddAppointmentForm)

appointment_delete = DeleteView.as_view(model=Appointment, success_url=reverse_lazy('appointment:appointment_list'))

