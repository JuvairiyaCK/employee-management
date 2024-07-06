from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('chome',HomeView.as_view(),name='chome'),
    path('empadd',EmployeeView.as_view(),name='aemp'),
    path('elist',EmpListView.as_view(),name='elist'),
    path('emdel/<int:eid>',RemoveEmpView.as_view(),name='emdel'),
    path('emedit/<int:eid>',EditEmpView.as_view(),name='emedit'),

]