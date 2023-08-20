from typing import Any
from django.db import models
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.views import View
from django.views.generic import ListView, UpdateView, DeleteView
from .models import Course, Professor, Classroom, TimeSlot
from .forms import CourseForm, ProfessorForm, ClassroomForm, TimeSlotForm

# Create your views here.
class IndexView(TemplateView):
    template_name = 'timetable/index.html'

class CreateCourseView(View):
    template_name = 'timetable/create_course.html'
    form_class = CourseForm
    success_url = '/'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {
            'form': form, 
        })
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        return render(request, self.template_name, {
            'form': form,
        })
    
class CreateProfessorView(View):
    template_name = 'timetable/create_professor.html'
    form_class = ProfessorForm
    success_url = '/'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {
            'form': form, 
        })
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        return render(request, self.template_name, {
            'form': form,
        })
    

class CreateClassroomView(View):
    template_name = 'timetable/create_classroom.html'
    form_class = ClassroomForm
    success_url = '/'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {
            'form': form, 
        })
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        return render(request, self.template_name, {
            'form': form,
        })
    

class CreateTimeSlotView(View):
    template_name = 'timetable/create_timeslot.html'
    form_class = TimeSlotForm
    success_url = '/'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {
            'form': form, 
        })
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        return render(request, self.template_name, {
            'form': form,
        })
    
class CourseUpdateView(UpdateView):
    model = Course
    fields = '__all__'
    template_name = 'timetable/create_course.html'

    def get_success_url(self):
        return reverse('all_data')
    
class CourseDeleteView(DeleteView):
    model = Course
    fields = '__all__'
    template_name = 'timetable/create_course.html'

    def get_success_url(self):
        return reverse('all_data')

class ProfessorUpdateView(UpdateView):
    model = Professor
    fields = ['name', 'courses_taught']
    template_name = 'timetable/create_professor.html'
    def get_success_url(self) -> str:
        return reverse('all_data')
    
class ProfessorDeleteView(DeleteView):
    model = Professor
    template_name = 'timetable/create_professor.html'

    def get_success_url(self) -> str:
        return reverse('all_data')
    
class ClassroomUpdateView(UpdateView):
    model = Classroom
    fields = '__all__'
    template_name = 'timetable/create_classroom.html'

    def get_success_url(self) -> str:
        return reverse('all_data')
    
class ClassroomDeleteView(DeleteView):
    model = Classroom
    template_name = 'timetable/create_classroom.html'

    def get_success_url(self) -> str:
        return reverse('all_data')
    
class TimeSlotUpdateView(UpdateView):
    model = TimeSlot
    fields = '__all__'
    template_name = 'timetable/create_timeslot.html'

    def get_success_url(self) -> str:
        return reverse('all_data')
    
class TimeSlotDeleteView(DeleteView):
    model = TimeSlot
    template_name = 'timetable/create_timeslot.html'

    def get_success_url(self) -> str:
        return reverse('all_data')
    
class AllDataView(View):
    template_name = 'timetable/all_data.html'

    def get(self, request):
        courses = Course.objects.all().order_by('name')
        professors = Professor.objects.all().order_by('name')
        classrooms = Classroom.objects.all().order_by('name')
        timeslots = TimeSlot.objects.all().order_by('start_time')

        return render(request, self.template_name, {
            'courses': courses,
            'professors': professors,
            'classrooms': classrooms,
            'timeslots': timeslots,
        })
    
    