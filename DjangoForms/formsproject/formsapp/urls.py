from django.urls import path
from . import views

urlpatterns = [
    path('teacher/', views.add_teacher, name='add_teacher'),
    path('teachers/', views.list_teachers, name='teachers'),
    path('group/', views.add_group, name='add_group'),
    path('groups/', views.list_groups, name='groups'),
]
