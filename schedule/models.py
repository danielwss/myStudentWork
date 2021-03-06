from django.db import models
from django.urls import reverse


class Lesson(models.Model):
    name = models.CharField(verbose_name='Название предмета', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ['name']


class Class(models.Model):
    a = 'А'
    b = 'Б'
    v = 'В'
    g = 'Г'
    class_name = [
        (a, 'А'),
        (b, 'Б'),
        (v, 'В'),
        (g, 'Г'),
    ]
    name = models.CharField(verbose_name='Класс', choices=class_name, max_length=50)
    class_number = models.IntegerField(blank=True, null=True)
    school_name = models.ForeignKey('School', verbose_name='Название школы', on_delete=models.PROTECT, related_name='сlasses', blank=True, null=True)

    def __str__(self):
        return f'{self.name}{self.class_number}'

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'
        ordering = ['school_name', 'class_number', 'name']


class Weekday(models.Model):
    monday = 'Понедельник'
    tuesday = 'Вторник'
    wednesday = 'Среда'
    thursday = 'Четверг'
    friday = 'Пятница'
    saturday = 'Суббота'
    week_day = [
        (monday, 'Понедельник'),
        (tuesday, 'Вторник'),
        (wednesday, 'Среда'),
        (thursday, 'Четверг'),
        (friday, 'Пятница'),
        (saturday, 'Суббота'),
    ]
    name = models.CharField(verbose_name='День недели', max_length=20, choices=week_day, blank=False, default=monday)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'День недели'
        verbose_name_plural = 'Дни недели'
        ordering = ['pk']


class LessonTime(models.Model):
    first = '1'
    second = '2'
    third = '3'
    fourth = '4'
    fifth = '5'
    sixth = '6'
    seventh = '7'
    eighth = '8'
    lesson_time = [
        (first, '1'),
        (second, '2'),
        (third, '3'),
        (fourth, '4'),
        (fifth, '5'),
        (sixth, '6'),
        (seventh, '7'),
        (eighth, '8'),
    ]
    time = models.CharField(verbose_name='Номер урока', max_length=5, choices=lesson_time, blank=False, default=first)
    name = models.CharField(verbose_name='Название', max_length=10, blank=True)

    def __str__(self):
        return self.time

    class Meta:
        verbose_name = 'Номер урока'
        verbose_name_plural = 'Номера уроков'
        ordering = ['pk']


class Audience(models.Model):
    audience = models.CharField(verbose_name='Аудитория', max_length=5)
    school_name = models.ForeignKey('School', verbose_name='Название школы', on_delete=models.PROTECT, related_name='audiences', blank=True, null=True)

    def __str__(self):
        return self.audience

    class Meta:
        verbose_name = 'Аудитория'
        verbose_name_plural = 'Аудитории'
        ordering = ['audience', 'school_name']


class School(models.Model):
    school_name = models.CharField(verbose_name='Школа', max_length=100, blank=True, default='ГУО СШ№')
    school_number = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.school_name}{self.school_number}'

    class Meta:
        verbose_name = 'Школа'
        verbose_name_plural = 'Школы'
        ordering = ['school_number']


class Teacher(models.Model):
    teacher_last_name = models.CharField(verbose_name='Фамилия учителя', max_length=50)
    teacher_first_name = models.CharField(verbose_name='Имя учителя', max_length=50)
    teacher_middle_name = models.CharField(verbose_name='Отчество учителя', max_length=50)
    school_name = models.ForeignKey('School', verbose_name='Название школы', on_delete=models.PROTECT, related_name='teachers', blank=True, null=True)

    def __str__(self):
        return f'{self.teacher_last_name} {self.teacher_first_name} {self.teacher_middle_name}'

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'
        ordering = ['teacher_last_name', 'school_name']


class Schedule(models.Model):
    school = models.ForeignKey('School', verbose_name='Школа', on_delete=models.PROTECT, blank=True, null=True)
    lesson = models.ForeignKey('Lesson', verbose_name='Урок', on_delete=models.PROTECT)
    s_class = models.ForeignKey('Class', verbose_name='Класс', on_delete=models.PROTECT)
    weekday = models.ForeignKey('Weekday', verbose_name='День недели', on_delete=models.PROTECT)
    lesson_time = models.ForeignKey('LessonTime', verbose_name='Номер урока', on_delete=models.PROTECT)
    audience = models.ForeignKey('Audience', verbose_name='Аудитория', on_delete=models.PROTECT)
    teacher = models.ForeignKey('Teacher', verbose_name='ФИО учителя', on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.s_class}{self.weekday}{self.lesson_time}{self.lesson}{self.audience}{self.teacher}{self.school}'

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписание'
        # unique_together = ('school', 'teacher', 'audience', 'lesson_time')
        ordering = ['weekday', 'lesson_time']
