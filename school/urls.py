"""
URL configuration for school project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from result.views import index_view
from result.views import student_view
from result.views import class_list_view
from result.views import guardian_view
from result.views import subject_view
from result.views import add_guardian_view,edit_guardian_view,delete_guardian_view
from result.views import add_student_view,edit_student_view,delete_student_view
from result.views import add_subject_view,edit_subject_view,delete_subject_view
from result.views import add_class_view, edit_class_view, delete_class_view
from result.views import add_academic_class_view,edit_academic_class_view,delete_academic_class_view
from result.views import add_grading_view, edit_grading_view ,delete_grading_view
from result.views import add_exam_view,edit_exam_view,delete_exam_view
from result.views import add_result_view,edit_result_view,delete_result_view,sign_up_view





urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    path('sign_up',sign_up_view, name = "sign_up_page"),
    path('', index_view, name='index_page'),
    path('student/', student_view, name='student_registered'),
    path('class/', class_list_view, name='class_page'),
    path('guardian/', guardian_view, name='guardian_page'),
    path('subject/', subject_view, name='subjects_page'),
    path ('add_guardian/',add_guardian_view , name= "add_guardian_page"),
    path('edit_guardian/<int:guardian_id>/',edit_guardian_view,name="edit_guardian_page"),
    path('delete_guardian/<int:guardian_id>/',delete_guardian_view ,name="delete_guardian"),
    path('add_student/',add_student_view,name="add_student_page"),
    path('edit_student/<int:student_id>/',edit_student_view,name="edit_student_page"),
    path('delete_student/<int:student_id>/',delete_student_view ,name="delete_student"),
    path('add_subject/',add_subject_view,name="add_subject_page"),
    path('edit_subject/<int:subject_id>/',edit_subject_view, name="edit_subject_page"),
    path('delete_subject/<int:subject_id>/',delete_subject_view, name="delete_subject_page"),
    path('add_class/', add_class_view, name='add_class_page'),
    path('edit_class/<int:class_id>/', edit_class_view, name='edit_class_page'),
    path('delete_class/<int:class_id>/', delete_class_view, name='delete_class_page'),
    path('add_academic_class/',add_academic_class_view ,name = "add_academic_class_page"),
    path('edit_academic_class/<int:academic_class_id>',edit_academic_class_view, name="edit_academic_class_page"),
    path('delete_academic_class/<int:academic_class_id>',delete_academic_class_view,name="delete_academic_class"),
    path('add_grading/',add_grading_view, name = 'add_grading_page'),
    path('edit_grading/<int:grading_id>/',edit_grading_view , name ="edit_grading_page"),
    path ('delete_grading/<int:grading_id>/',delete_grading_view, name = 'delete_grading_page'),
    path('add_exam/',add_exam_view ,name = 'add_exam_page'),
    path('edit_exam/<int:exam_id>/',edit_exam_view , name="edit_exam_page"),
    path('delete_exam/<int:exam_id>/',delete_exam_view , name= 'delete_exam_page'),
    path ('add_result/' ,add_result_view , name = 'add_result_page'),
    path ('edit_result/<int:result_id>/',edit_result_view , name ='edit_result_page'),
    path ('delete_result/<int:result_id>/',delete_result_view , name ='delete_result_page'),
    


  

    


    
]
