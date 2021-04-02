from django.urls import path

from . import views
from .views import *
from .forms import *

urlpatterns = [
   # path('', IndexView.as_view(), name='home'),
    path('', IndexView.as_view(), name='home'),
    path('natch/', NatchView.as_view(), name='natch'),
    path('sred/', SredView.as_view(), name='sred'),
    path('add/', AddScheduleView.as_view(), name='add_schedule'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
