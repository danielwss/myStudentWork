from django.contrib.auth import login, logout
from django.db import connection
from django.forms import Form
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.backends import django
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.views.generic.base import View

from .forms import UserLoginForm, ScheduleForm, ScheduleAddForm
from .models import *


#
#
#
#

## Темплей вьюхи(Главная, 1-4, 5-9)
class IndexView(TemplateView):
    template_name = 'schedule/schools.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['schools'] = School.objects.all()
        return context


class ClassList(View):
    def get(self, request, id):
        school = School.objects.get(id=id)
        classes = Class.objects.filter(school_name=school)
        context = {'school': school, 'classes': classes}
        return render(request, 'schedule/index.html', context)


class ScheduleView(View):
    def get(self, request, class_id):
        class_name = Class.objects.get(id=class_id)
        schedules = Schedule.objects.filter(s_class=class_name)
        form = ScheduleForm()
        teachers = Teacher.objects.filter(school_name=class_name.school_name)
        audiences = Audience.objects.filter(school_name=class_name.school_name)
        context = {'class_name': class_name, 'schedules': schedules, 'form': form, 'teachers': teachers, 'audiences': audiences}
        return render(request, 'schedule/schedule.html', context)

    def post(self, request, class_id):
        class_name = Class.objects.get(id=class_id)
        school = School.objects.get(id=class_name.school_name.id)
        form = ScheduleForm(request.POST)
        if form.is_valid():
            print(request.POST)
            print(request.POST.getlist('teachers')[0])
            audience = Audience.objects.get(audience=request.POST.getlist('audiences')[0], school_name = school)
            teacher = Teacher.objects.get(id=request.POST.getlist('teachers')[0])
            schedule = Schedule.objects.create(weekday=form.cleaned_data['weekday'],
                                               lesson_time=form.cleaned_data['lesson_time'],
                                               lesson=form.cleaned_data['lesson'],
                                               audience=audience,
                                               teacher=teacher,
                                               school=school,
                                               s_class=class_name)
            return redirect('scheduleview', class_id=class_name.id)
        return redirect('scheduleview', class_id=class_name.id)

## Добавление записей

class AddScheduleView(CreateView):
    form_class = ScheduleAddForm
    template_name = 'schedule/add.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить урок в расписание'
        return context


## Auth


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'authorization.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')
