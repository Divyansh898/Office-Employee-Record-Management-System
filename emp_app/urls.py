"""Office_mana_Sys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path ,include
from .import views

urlpatterns = [
   path('',views.index,name='index'),
   path('registration',views.registartion,name='registration'),
   path('emp_login',views.emp_login,name='emp_login'),
   path('emp_home',views.emp_home,name='emp_home'),
   path('profile',views.profile,name='profile'),
   path('logout',views.Logout,name='logout'),
   path('admin_login',views.admin_login,name='admin_login'),
   path('my_experience',views.my_experience,name='my_experience'),
   path('edit_experience',views.edit_experience,name='edit_experience'),
   path('my_education',views.my_education,name='my_education'),
   path('edit_myeducation',views.edit_myeducation,name='edit_myeducation'),
   path('change_password',views.change_password,name='change_password'),
   path('admin_home',views.admin_home,name='admin_home'),
   path('change_passwordadmin',views.change_passwordadmin,name='change_passwordadmin'),
   path('all_employee',views.all_employee,name='all_employee'),
   path('delete_employee<int:pid>',views.delete_employee,name='delete_employee'),
   path('edit_profile<int:pid>',views.edit_profile,name='edit_profile'),
   path('edit_education<int:pid>',views.edit_education,name='edit_education'),
   path('edit_adminexperience<int:pid>',views.edit_adminexperience,name='edit_adminexperience'),

   
]
