from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class customUser(AbstractUser):
    is_user = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superAdmin = models.BooleanField(default=False)
    address = models.CharField(max_length=200)
    contact_no = models.CharField(max_length=50)
    
    def __str__(self):
        if self.is_user:
            return f"user - {self.first_name} {self.last_name}"
        elif self.is_staff:
            return f"staff - {self.first_name} {self.last_name}"
        elif self.is_admin:
            return f"admin - {self.first_name} {self.last_name}"
        elif self.is_superAdmin:
            return f"superAdmin - {self.first_name} {self.last_name}"
        
        
class Customer_state(models.Model):
    customer_state_id = models.AutoField(primary_key=True)
    customer_state = models.CharField(max_length=20)
    
    def __str__(self):
        return self.customer_state
    

class User_state(models.Model):
    user_state_id = models.AutoField(primary_key=True)
    user_state = models.CharField(max_length=50)
    
    def __str__(self):
        return self.user_state

class Staff_category(models.Model):
    staff_category_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=50)
    rank = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.category} - {self.rank}"

class Attendance(models.Model):
    attendance_id = models.AutoField(primary_key=True)
    attendance = models.CharField(max_length=10)
    
    
    def __str__(self):
        return self.attendance
    
class Reservation_state(models.Model):
    reservation_state_id = models.AutoField(primary_key=True)
    reservation_state = models.CharField(max_length=50)
    
    def __str__(self):
        return self.reservation_state
    
class Order_state(models.Model):
    order_state_id = models.AutoField(primary_key=True)
    order_state = models.CharField(max_length=50)
    
    def __str__(self):
        return self.order_state

class Ordered_food_state(models.Model):
    ordered_food_state_id = models.AutoField(primary_key=True)
    ordered_food_state = models.CharField(max_length=100)
    
    def __str__(self):
        return self.ordered_food_state
    
class Order_food_state(models.Model):
    order_food_state_id = models.AutoField(primary_key=True)
    order_food_state = models.CharField(max_length=100)
    
    def __str__(self):
        return self.order_food_state
    
class Payment_type(models.Model):
    payment_type_id = models.AutoField(primary_key=True)
    payment_type = models.CharField(max_length=20)
    
    def __str__(self):
        return self.payment_type
    
class Manager(models.Model):
    manager_id = models.AutoField(primary_key=True)
    user_state_id = models.ForeignKey(User_state, on_delete=models.SET_NULL, null=True)
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    contact_no = models.CharField(max_length=50)
    
    def __str__(self):
        return f"Manager {self.manager_id} - {self.f_name} {self.l_name}"
    
class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    manager_id = models.ForeignKey(Manager, on_delete=models.SET_NULL, null=True)
    staff_category_id = models.ForeignKey(Staff_category, on_delete=models.SET_NULL, null=True)
    user_state_id = models.ForeignKey(User_state, on_delete=models.SET_NULL, null=True)
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    contact_no = models.CharField(max_length=50)
    
    def __str__(self):
        return f"staff {self.staff_category_id} {self.staff_id} - {self.f_name} {self.l_name}" 
    
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_state = models.ForeignKey(Customer_state, on_delete=models.SET_NULL,null=True)
    staff_id = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True)
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    contact_no = models.CharField(max_length=50)
    
    def __str__(self):
        return f"Customer {self.customer_id} - {self.f_name} {self.l_name}"
    
class Manager_login_info(models.Model):
    manager_login_info_id = models.AutoField(primary_key=True)
    manager_id = models.ForeignKey(Manager, on_delete=models.SET_NULL, null=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(50)
    
    def __str__(self):
        return f'manager login info {self.manager_id} - {self.username}'
    
class Manager_login(models.Model):
    manager_login_id =  models.AutoField(primary_key=True)
    manager_id = models.ForeignKey(Manager, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.manager_id} - {self.created_at}'

class Staff_login_info(models.Model):
    staff_login_info_id = models.AutoField(primary_key=True)
    manager_id = models.ForeignKey(Manager, on_delete=models.SET_NULL, null=True)
    staff_id = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(50)
    
    def __str__(self):
        return f'manager login info {self.staff_id} - {self.username}'
    
class Staff_login(models.Model):
    staff_login_id =  models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.staff_id} - {self.created_at}'
    
    
class Customer_login_info(models.Model):
    customer_login_info_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(50)
    
    def __str__(self):
        return f'manager login info {self.customer_id} - {self.email}'
    
class Customer_login(models.Model):
    customer_login_id =  models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.customer_id} - {self.created_at}'
    
class Stock(models.Model):
    stock_id = models.AutoField(primary_key=True)
    manager_id = models.ForeignKey(Manager, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    qty = models.CharField(max_length=50)
    
    def __str__(self):
        return f'stock {self.stock_id} - {self.name} - {self.qty}'
    
class Menu(models.Model):
    menu_id = models.AutoField(primary_key=True)
    manager_id = models.ForeignKey(Manager, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='menu_images/', null=True, blank=True)
    name = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    ratings = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    keywords = models.TextField()
    availability = models.CharField(max_length=20)
    
    def __str__(self):
        return f'{self.menu_id} {self.name}'
    
class Salary(models.Model):
    salary_id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True)
    basic = models.DecimalField(max_digits=10, decimal_places=2)
    bonus = models.DecimalField(max_digits=10, decimal_places=2)
    overtime = models.DecimalField(max_digits=10, decimal_places=2)
    overtime_rate = models.DecimalField(max_digits=10, decimal_places=2)
    epf_employee = models.IntegerField()#8%
    gross_salary = models.DecimalField(max_digits=10, decimal_places=2)
    net_salary = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f'salary {self.salary_id} - {self.staff_id}'
    
class SalaryHistory(models.Model):
    salary_history_id = models.AutoField(primary_key=True)
    salary_id = models.ForeignKey(Salary, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f'SalaryHistory {self.salary_history_id} - {self.salary_id}'
    
class Staff_attendance(models.Model):
    staff_attendance_id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True)
    attendance_id = models.ForeignKey(Attendance, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(default=timezone.now)
    overtime = models.IntegerField()
    
    def __str__(self):
        return f'attendance {self.date} - {self.staff_id} - {self.attendance_id}'
    
class Feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    food_id = models.ForeignKey(Menu, on_delete=models.SET_NULL, null=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    feedback = models.TextField()
    ratings = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f'feedback {self.food_id} - {self.feedback}'
    
class Cart(models.Model):
    item_id = models.AutoField(primary_key=True)
    food_id = models.ForeignKey(Menu, on_delete=models.SET_NULL, null=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f'cart {self.customer_id} - {self.food_id}'
    
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    item_id = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True)
    staff_id = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True)
    order_state_id = models.ForeignKey(Order_state, on_delete=models.SET_NULL, null=True)
    total_fee = models.DecimalField(max_digits=10, decimal_places=2)
    ordered_at = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return f'order {self.customer_id} - {self.order_id} - {self.total_fee}'

class Ordered_food(models.Model):
    ordered_food_id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    food_id = models.ForeignKey(Menu, on_delete=models.SET_NULL, null=True)
    staff_id = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True)
    ordered_food_state_id = models.ForeignKey(Ordered_food_state, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f'ordered food {self.ordered_food_id} - {self.order_id} - {self.food_id}'
    
class Order_payment(models.Model):
    order_payment_id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    payment_type_id = models.ForeignKey(Payment_type, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f'order payment {self.order_id} - {self.payment_type_id}'
    
class Table_info(models.Model):
    table_id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True)
    seats = models.IntegerField()
    
    def __str__(self):
        return f'table info {self.table_id} - {self.seats}'
    
class Reservation(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    staff_id = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True)
    reservation_state_id = models.ForeignKey(Reservation_state, on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    time = models.TimeField()
    
    def __str__(self):
        return f'reservation {self.customer_id} - {self.reservation_id}'
    
class Reserved_tables(models.Model):
    reserved_tables_id = models.AutoField(primary_key=True)
    reservation_id = models.ForeignKey(Reservation, on_delete=models.SET_NULL, null=True)
    table_id = models.ForeignKey(Table_info, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f'reserved_tables {self.reservation_id} - {self.table_id}'
    
class Reservation_payment(models.Model):
    reservation_payment_id = models.AutoField(primary_key=True)
    reservation_id = models.ForeignKey(Reservation, on_delete=models.SET_NULL, null=True)
    payment_type_id =  models.ForeignKey(Payment_type, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'reservation_payment {self.reservation_id} - {self.payment_type_id}'
    