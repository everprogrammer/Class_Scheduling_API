from django.urls import path
from .  import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create-course/', views.CreateCourseView.as_view(), name='create-course'),
    path('create-professor/', views.CreateProfessorView.as_view(), name='create-professor'),
    path('create-timeslot/', views.CreateTimeSlotView.as_view(), name='create-timeslot'),
    path('create-classroom/', views.CreateClassroomView.as_view(), name='create-classroom'),
    path('update_course/<int:pk>', views.CourseUpdateView.as_view(), name='update_course'),
    path('delete_course/<int:pk>', views.CourseDeleteView.as_view(), name='delete_course'),
    path('update_professor/<int:pk>', views.ProfessorUpdateView.as_view(), name='update_professor'),
    path('delete_professor/<int:pk>', views.ProfessorDeleteView.as_view(), name='delete_professor'),
    path('update_classroom/<int:pk>', views.ClassroomUpdateView.as_view(), name='update_classroom'),
    path('delete_classroom/<int:pk>', views.ClassroomDeleteView.as_view(), name='delete_classroom'),
    path('update_timeslot/<int:pk>', views.TimeSlotUpdateView.as_view(), name='update_timeslot'),
    path('delete_timeslot/<int:pk>', views.TimeSlotDeleteView.as_view(), name='delete_timeslot'),
    path('all-data/', views.AllDataView.as_view(), name='all_data'),
]