from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import TemplateView

from app.models import Employees


# class MainView(TemplateView):
#     template_name = "index.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['custom_data'] = Employees.objects.all()
#
#         return context
#
#     def post(self, request, *args, **kwargs):
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         address = request.POST.get('address')
#         phone = request.POST.get('phone')
#
#         emp = Employees.objects.create(
#             name=name,
#             email=email,
#             address=address,
#             phone=phone
#         )
#         return redirect('main-view')
#
#     def deleta(self, request, *args, **kwargs):
#         employee_id = request.POST.get('employee_id')
#
#         try:
#             employee = Employees.objects.get(pk=employee_id)
#             employee.delete()
#         except Employees.DoesNotExist:
#             pass
#
#         return redirect('main-view')


def INDEX(request):
    emp = Employees.objects.all()

    context = {
        "emp": emp,
    }
    return render(request, "index.html", context)


def ADD(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = Employees(
            name=name,
            email=email,
            address=address,
            phone=phone
        )
        emp.save()
        return redirect('home')


    return render(request, "index.html")


def EDIT(request):
    emp = Employees.objects.all()

    context = {
        "emp": emp,
    }
    return render(request, "index.html", context)


def UPDATE(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = Employees(
            id=id,
            name=name,
            email=email,
            address=address,
            phone=phone
        )
        emp.save()
        return redirect('home')
    return redirect('home')


def DELETE(request, id):
    emp = Employees.objects.get(pk=id)
    emp.delete()
    return redirect('home')