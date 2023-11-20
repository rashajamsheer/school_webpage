from django.contrib import admin
from . import views
from django.urls import path
app_name='schoolapp'
urlpatterns = [
   path('',views.index,name='index'),
   path('register',views.register,name='register'),
   path('login',views.login,name='login'),
   path('logout',views.logout,name='logout'),
   path('new/',views.new,name='new'),
   path('student_form/', views.student_form, name='student_form'),
   path('ajax/load-courses/',views.load_courses, name='ajax_load_courses'),
   path('',views.allCourceDep,name='allCourceDep'),
]