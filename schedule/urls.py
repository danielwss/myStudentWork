from django.urls import path

from . import views
from .views import *
from .forms import *

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('add/', AddScheduleView.as_view(), name='add_schedule'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('<int:id>/', ClassList.as_view(), name='classlist'),
    path('<int:class_id>', ScheduleView.as_view(), name='scheduleview'),
    path('<int:class_id>/scheduleupdate/<int:schedule_id>/', ScheduleUpdate.as_view(), name='scheduleupdate'),
    path('<int:class_id>/scheduledelete/<int:schedule_id>/', ScheduleDelete.as_view(), name='scheduledelete'),
    path('teachers/<int:school_id>/', Teachers.as_view(), name='teachers'),
    path('teacherschedule/<int:teacher_id>/', TeacherSchedule.as_view(), name='teacherschedule'),

]
