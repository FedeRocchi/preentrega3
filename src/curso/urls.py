
from django.urls import path
from . import views

app_name = 'curso'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('about/', views.about),
    path('curso/list/', views.curso_list, name='curso_list'),
    path('curso/create/', views.curso_create, name='curso_create'),
    path('alumno/list/', views.alumno_list, name='alumno_list'),
    path('alumno/create/', views.alumno_create, name='alumno_create'),
    path('comision/list/', views.comision_list, name='comision_list'),
    path('comision/create/', views.comision_create, name='comision_create'),
    

]