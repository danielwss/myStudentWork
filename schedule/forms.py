from django.contrib.auth.forms import AuthenticationForm
from django import forms

from schedule.models import Schedule


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['lesson', 'weekday', 'lesson_time']


class ScheduleAddForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['school', 's_class', 'weekday', 'lesson_time', 'lesson', 'audience', 'teacher']