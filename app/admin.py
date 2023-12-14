from django.contrib import admin
from app.models import Employees


class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'address', 'phone')


admin.site.register(Employees, EmployeesAdmin)

