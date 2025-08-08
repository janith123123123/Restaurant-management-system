from django.urls import path
from . import views

urlpatterns = [
    path("",views.manager, name="manager"),
    path("manage_staff/",views.manage_staff, name="manage_staff"),
    path("manage_menu/",views.manage_menu, name="manage_menu"),
    path("manage_stock/",views.manage_stock, name="manage_stock"),
    path("staff_member/<int:staff_id>/",views.staff_member, name="staff_member"),
    path("add_staff_member/",views.add_staff_member, name="add_staff_member"),
    path("edit_staff_info/<int:staff_id>/",views.edit_staff_info, name="edit_staff_info"),
    path("edit_menu_item/",views.edit_menu_item, name="edit_menu_item"),
]
