from django.contrib import admin
from .storemodels import Employee
from .storework import Worksubmit


admin.site.register(Employee)
admin.site.register(Worksubmit)
# Register your models here.
