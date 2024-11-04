from django.db import models

dept_choices=(
            ('HR','HR'),
            ('Engineering','Engineering'),
            ('Sales','Sales'),
            ('Accounts','Accounts'),
)
role_choices=(
            ('Manager','Manager'),
            ('Developer','Developer'),
            ('Analyst','Analyst'),
            ('Customer Executive','Customer Executive'),
)

# Create your models here.
class Emp(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=300)
    department=models.CharField(max_length=100,choices=dept_choices,default=None)
    role=models.CharField(max_length=100,choices=role_choices,default=None)
    date_joined=models.DateField(auto_now_add=True)
