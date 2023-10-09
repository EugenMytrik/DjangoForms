from django.shortcuts import render, redirect
from .models import Teacher, Group
from .forms import TeacherForm, GroupForm


def add_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teachers')
    else:
        form = TeacherForm()
    return render(request, 'add_teacher.html', {'form': form})


def list_teachers(request):
    teachers = Teacher.objects.all()
    return render(request, 'list_teachers.html', {'teachers': teachers})


def add_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('groups')
    else:
        form = GroupForm()
    return render(request, 'add_group.html', {'form': form})


def list_groups(request):
    groups = Group.objects.all()
    return render(request, 'list_groups.html', {'groups': groups})
