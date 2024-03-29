from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DeleteView
from .models import TeacherData
from django.urls import reverse_lazy
# Create your views here.

class TeacherInfo(ListView):
    model = TeacherData
    template_name = 'teacher_info.html'

class TeacherInfoUpdate(UpdateView):
    model = TeacherData
    template_name = 'edit_teacher_data.html'
    fields = ('teacherfio','kasbi','teacher_info')

class TeacherInfoDelete(DeleteView):
    model = TeacherData
    template_name = 'delete_teacher_data.html'
    success_url = reverse_lazy('teacher_info')