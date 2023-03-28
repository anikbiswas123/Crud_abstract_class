from django.shortcuts import render, redirect
from .models import *


# Create your views here.
def show_emp(request):
    emp_list = emplopyee.objects.all()
    return render(request, 'emplopyee_show.html', locals())


def show_cus(request):
    cust_list = customer.objects.all()
    return render(request, 'customer_show.html', locals())


def add_employee(request):
    if request.method == 'POST':
        EMP_name = request.POST.get('emp_name')
        emp_post = request.POST.get('emp_post')
        emp_salary = request.POST.get('emp_salary')
        distr = request.POST.get('distr')
        sub_distr = request.POST.get('sub_distr')
        address = request.POST.get('address')

        emp = emplopyee()
        emp.emp_name = EMP_name
        emp.emp_post = emp_post
        emp.emp_salary = emp_salary
        emp.distr = distr
        emp.sub_distr = sub_distr
        emp.address = address
        emp.save()
        return redirect(show_emp)
    return render(request, 'add_employee.html')


def add_customer(request):
    if request.method == 'POST':
        cust_name = request.POST.get('cust_name')
        cust_email = request.POST.get('cust_email')
        cust_phone = request.POST.get('cust_Phon')
        distr = request.POST.get('distr')
        sub_distr = request.POST.get('sub_distr')
        address = request.POST.get('address')

        cust = customer()
        cust.cust_name = cust_name
        cust.cust_email = cust_email
        cust.cust_Phon = cust_phone
        cust.distr = distr
        cust.sub_distr = sub_distr
        cust.address = address
        cust.save()
        return redirect(show_cus)
    return render(request, 'add_customer.html')


def delete_emp(request, id):
    emp = emplopyee.objects.get(id=id)
    emp.delete()
    return redirect(show_emp)

def delete_cust(request,id):
    cust=customer.objects.get(id=id)
    cust.delete()
    return redirect(show_cus)

