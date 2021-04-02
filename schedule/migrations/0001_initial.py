# Generated by Django 3.1.6 on 2021-04-02 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audience', models.CharField(max_length=5, verbose_name='Аудитория')),
            ],
            options={
                'verbose_name': 'Аудитория',
                'verbose_name_plural': 'Аудитории',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Класс')),
            ],
            options={
                'verbose_name': 'Класс',
                'verbose_name_plural': 'Классы',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название предмета')),
            ],
            options={
                'verbose_name': 'Урок',
                'verbose_name_plural': 'Уроки',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='LessonTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], default='1', max_length=5, verbose_name='Номер урока')),
                ('name', models.CharField(blank=True, max_length=10, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Номер урока',
                'verbose_name_plural': 'Номера уроков',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_last_name', models.CharField(max_length=50, verbose_name='Фамилия учителя')),
                ('teacher_first_name', models.CharField(max_length=50, verbose_name='Имя учителя')),
                ('teacher_middle_name', models.CharField(max_length=50, verbose_name='Отчество учителя')),
            ],
            options={
                'verbose_name': 'Учитель',
                'verbose_name_plural': 'Учителя',
                'ordering': ['teacher_last_name'],
            },
        ),
        migrations.CreateModel(
            name='Weekday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Понедельник', 'Понедельник'), ('Вторник', 'Вторник'), ('Среда', 'Среда'), ('Четверг', 'Четверг'), ('Пятница', 'Пятница'), ('Суббота', 'Суббота')], default='Понедельник', max_length=20, verbose_name='День недели')),
            ],
            options={
                'verbose_name': 'День недели',
                'verbose_name_plural': 'Дни недели',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audience', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='schedule.audience', verbose_name='Аудитория')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='schedule.lesson', verbose_name='Урок')),
                ('lesson_time', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='schedule.lessontime', verbose_name='Номер урока')),
                ('s_class', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='schedule.class', verbose_name='Класс')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='schedule.teacher', verbose_name='ФИО учителя')),
                ('weekday', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='schedule.weekday', verbose_name='День недели')),
            ],
            options={
                'verbose_name': 'Расписание',
                'verbose_name_plural': 'Расписание',
                'ordering': ['pk'],
            },
        ),
    ]
