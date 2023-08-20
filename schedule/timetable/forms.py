from django import forms
from .models import Course, Professor, Classroom, TimeSlot

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = '__all__'

class ClassroomForm(forms.ModelForm):
    class Meta:
        model = Classroom
        fields = '__all__'

class TimeSlotForm(forms.ModelForm):
    class Meta:
        model = TimeSlot
        fields = '__all__'