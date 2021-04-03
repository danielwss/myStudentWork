from django.urls import path

from . import views
from .views import *
from .forms import *

urlpatterns = [
   # path('', IndexView.as_view(), name='home'),
    path('', IndexView.as_view(), name='home'),
    path('add/', AddScheduleView.as_view(), name='add_schedule'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('<int:id>/', ClassList.as_view(), name='classlist'),
    path('<int:class_id>', ScheduleView.as_view(), name='scheduleview'),

]
