from django.contrib.auth import login, logout
from django.db import connection
from django.forms import Form
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from .forms import UserLoginForm, ScheduleForm
from .models import *


#
#
#
#

## Темплей вьюхи(Главная, 1-4, 5-9)
class IndexView(TemplateView):
    template_name = 'schedule/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context


class NatchView(TemplateView):
    template_name = 'schedule/1-4.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Певрые - четвёртые классы'
        return context


class SredView(TemplateView):
    template_name = 'schedule/5-9.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Пятые - девятые классы'
        return context


## CreateView


class CupsView(ListView):
    Model = Schedule
    context_object_name = 'schedule'
    template_name = 'schedule/schedule.html'
    # paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = ''
        return context

    def get_queryset(self):
        return Schedule.objects.all()



## Добавление записей

class AddScheduleView(CreateView):
    form_class = ScheduleForm
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
