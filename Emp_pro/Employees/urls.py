from django.urls import path
from Employees import views

app_name='Employees'

urlpatterns = [
    path("ind/",views.index,name="index"),
    path('add/',views.add,name="add"),
    path('edit/<int:emp_id>/',views.update,name="update"),
    path('del/<int:emp_id>/',views.delete,name="delete"),
    path('view/<int:emp_id>/',views.read,name="read"),
]