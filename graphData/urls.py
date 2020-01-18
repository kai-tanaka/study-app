from django.urls import path
from . import views

app_name = 'graphData'

urlpatterns = [
    path('index', views.index, name='index'),
    path('<int:id>/delete/', views.delete, name='delete'),
    path('graphData/<str:category>/',
         views.graphData_category, name='graphData_category'),
    path('new_category/', views.new_category, name='new_category'),
    path('new_graphData/', views.new_graphData, name='new_graphData'),
]
