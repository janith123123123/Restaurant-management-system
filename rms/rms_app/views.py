from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Staff, Salary, Menu, Staff_attendance
from .forms import StaffForm, EditStaffForm, EditSalaryForm
from datetime import datetime



# Create your views here.

def manager(response):
    return render(response,'manager.html',{})

def manage_staff(request):
    staff_members = Staff.objects.all()
    searched_staff = None
    searched = False
    
    staff_id = request.GET.get('staff_id')
    if staff_id:
        searched=True
        try:
            searched_staff = Staff.objects.get(pk=staff_id)
        except Staff.DoesNotExist:
            searched_staff = None
            
    return render(request,'manage_staff.html',{'staff_members':staff_members,
                                               'searched_staff':searched_staff,
                                               'searched':searched})
    
def manage_menu(request ):
    menu_items = Menu.objects.all()
    return render(request ,'manage_menu.html',{'menu_items':menu_items})

def manage_stock(response):
    return render(response,'manage_stock.html',{})

def staff_member(request, staff_id):
    staff = Staff.objects.get(pk=staff_id)
    category = staff.staff_category_id.category
    rank = staff.staff_category_id.rank
    manager = staff.manager_id
    state = staff.user_state_id.user_state
    
    salary = Salary.objects.get(staff_id=staff_id)
    attendances = Staff_attendance.objects.filter(staff_id=staff_id)
    
    from_date = request.GET.get('from_date')
    to_date = request.GET.get('to_date')
    
    formatted_attendances = []
    p = 0 
    a = 0
    l = 0
    total_overtimes = 0
    is_searched = False
    if from_date is not None and to_date is not None:
        is_searched = True
        for att in attendances:
            formatted_dt = att.date.strftime("%Y-%m-%d")
            if from_date <= formatted_dt <= to_date:
                total_overtimes += att.overtime
                formatted_attendances.append({'date':formatted_dt, 
                                              'data':[att.attendance_id.attendance,att.overtime]})

                if att.attendance_id.attendance == 'Present':
                    p += 1
                elif att.attendance_id.attendance == 'Absent':
                    a += 1
                else:
                    l += 1 
           
    return render(request,'staff_member.html',{'staff':staff,'category':category,
                                               'manager':manager,'state':state,
                                               'rank':rank,'salary':salary,
                                               'formatted_attendances':formatted_attendances,
                                               'to_date':to_date,'from_date':from_date,
                                               'is_searched':is_searched,'p':p,
                                               'a':a,'l':l,'total_overtimes':total_overtimes})

def add_staff_member(request):
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_staff')
        else:
            print(form.errors)
    else:
        form = StaffForm()
    return render(request,'add_staff_member.html',{'form':form})

def edit_staff_info(request, staff_id):
    staff = Staff.objects.get(pk=staff_id)
    salary = Salary.objects.get(staff_id=staff_id)
    attendances = Staff_attendance.objects.filter(staff_id=staff_id)
    total_overtimes = 0
    for att in attendances:
        total_overtimes += att.overtime
    staff_or_salary = request.GET.get('staff_or_salary')
    if staff_or_salary == 'staff info':
        if request.method == 'POST':
            edit_form = EditStaffForm(request.POST,instance=staff)
            if edit_form.is_valid():
                edit_form.save()
                
                gross_salary = salary.basic + salary.bonus + (salary.overtime * salary.overtime_rate)
                net_salary = gross_salary - (salary.epf_employee / 100 * gross_salary)
                salary.gross_salary = gross_salary
                salary.net_salary = net_salary
                salary.save()
                
                return redirect('staff_member',staff_id=staff.staff_id)
            else:
                print(edit_form.errors)
        else:
            edit_form = EditStaffForm(instance=staff)
    else:
        if request.method == 'POST':
            edit_form = EditSalaryForm(request.POST,instance=salary)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('staff_member',staff_id=staff.staff_id)
            else:
                print(edit_form.errors)
        else:
            edit_form = EditSalaryForm(instance=salary)
    return render(request,'edit_staff_info.html',{'staff':staff,'edit_form':edit_form,
                                                  'staff_or_salary':staff_or_salary})
    

def edit_menu_item(request ):
    menu_items = Menu.objects.all()
    return render(request ,'edit_menu_item.html',{'menu_items':menu_items})