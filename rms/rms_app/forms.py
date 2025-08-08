from django import forms
from .models import Staff, Salary

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['manager_id','staff_category_id','user_state_id',
                  'f_name','l_name','address','contact_no']
        
class EditStaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['staff_category_id','user_state_id',
                  'f_name','l_name','address','contact_no']
        
class EditSalaryForm(forms.ModelForm):
    class Meta:
        model = Salary
        fields = ['basic','bonus','overtime','epf_employee']
        