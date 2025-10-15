from django.shortcuts import render,redirect
from django.urls import reverse

from result.forms import GuardianForm,StudentForm,SubjectForm, ClassForm
from result.forms import AcademicClassForm
from result.models import AcademicClass
from result.models import Guardian,Student,Subject,Class




def index_view(request):
    return render (request,'index.html')


def student_view(request):
    return render(request, 'student.html')

def class_list_view(request):
    return render (request,'class.html')

def guardian_view (request):
    return render (request, 'guardian.html') 

def  subject_view (request):
    return render (request, 'subject.html')

#GUARDIAN
def add_guardian_view (request):
    message =''
    if request.method == "POST":
        guardian_form = GuardianForm(request.POST)

        if guardian_form.is_valid():
            guardian_form.save()
        
        message ="Guardian Succesfully Added"
    
    else:
        guardian_form = GuardianForm()
    
    guardians = Guardian.objects.all()
    


    context = { 
        'form':guardian_form,
        'msg': message,
        'guardians':guardians,
        
        }
    
    return render(request,"add_guardian.html",context)

def edit_guardian_view(request,guardian_id):
    guardian = Guardian.objects.get(id=guardian_id)
    message = ""
    if request.method == "POST":
        guardian_form = GuardianForm(request.POST,instance=guardian)

        if guardian_form.is_valid():
            guardian_form.save()
            message = "Changes saved Successfully"

        else :
            message = "form has valid data"
    else:
        guardian_form = GuardianForm(instance=guardian)
    context ={
        'form':guardian_form,
        'guardian':guardian,
        'message':message,
    }

    return render (request,'edit_guardian.html',context)




def delete_guardian_view(request, guardian_id):
    guardian = Guardian.objects.get(id=guardian_id)
    guardian.delete()
    return redirect('add_guardian_page')




#Student

def add_student_view (request):
    message =''
    if request.method == "POST":
        student_form = StudentForm(request.POST)

        if student_form.is_valid():
            student_form.save()
        
        message ="Student Succesfully Added"
    
    else:
        student_form = StudentForm()
    
    students = Student.objects.all()
    


    context = { 
        'form':student_form,
        'msg': message,
        'students':students,
        
        }
    
    return render(request,"add_student.html",context)





def edit_student_view(request,student_id):
    student = Student.objects.get(id=student_id)
    message = ""
    if request.method == "POST":
        student_form = StudentForm(request.POST,instance=student)

        if student_form.is_valid():
            student_form.save()
            message = "Changes saved Successfully"

        else :
            message = "form has valid data"
    else:
        student_form = StudentForm(instance=student)
    context ={
        'form':student_form,
        'student':student,
        'message':message,
    }

    return render (request,'edit_student.html',context)



def delete_student_view(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return redirect('add_student_page')

#SUBJECT

def add_subject_view (request):
    message =''
    if request.method == "POST":
        subject_form = SubjectForm(request.POST)

        if subject_form.is_valid():
            subject_form.save()
        
        message ="Subject Succesfully Added"
    
    else:
        subject_form = SubjectForm()
    
    subjects = Subject.objects.all()
    


    context = { 
        'form':subject_form,
        'msg': message,
        'subjects':subjects,
        
        }
    
    return render(request,"add_subject.html",context)



def edit_subject_view(request,subject_id):
    subject = Subject.objects.get(id=subject_id)
    message = ""
    if request.method == "POST":
        subject_form = SubjectForm(request.POST,instance=subject)

        if subject_form.is_valid():
            subject_form.save()
            message = "Changes saved Successfully"

        else :
            message = "form has valid data"
    else:
        subject_form = SubjectForm(instance=subject)
    context ={
        'form':subject_form,
        'subject':subject,
        'message':message,
    }

    return render (request,'edit_subject.html',context)




def delete_subject_view(request, subject_id):
    subject = Subject.objects.get(id=subject_id)
    subject.delete()
    return redirect('add_subject_page')



#CLASS

def add_class_view (request):
    message =''
    if request.method == "POST":
        class_form = ClassForm(request.POST)

        if class_form.is_valid():
            class_form.save()
        
        message ="Class Succesfully Added"
    
    else:
        class_form = ClassForm()
    
    class_s = Class.objects.all()
    


    context = { 
        'form':class_form,
        'msg': message,
        'class_s':class_s,
        
        }
    
    return render(request,"add_class.html",context)



def edit_class_view(request,class_id):
    class_s = Class.objects.get(id=class_id)
    message = ""
    if request.method == "POST":
        class_form = ClassForm(request.POST,instance=class_s)

        if class_form.is_valid():
            class_form.save()
            message = "Changes saved Successfully"

        else :
            message = "form has valid data"
    else:
        class_form = ClassForm(instance = class_s)
    context ={
        'form':class_form,
        'class_s':class_s,
        'message':message,
    }

    return render (request,'edit_class.html',context)




def delete_class_view(request, class_id):
    class_s = Class.objects.get(id=class_id)
    class_s.delete()
    return redirect('add_class_page')



#ACADEMIC CLASS


def add_academic_class_view(request):
    message = ''
    
    if request.method == "POST":
        academic_class_form = AcademicClassForm(request.POST)
        
        if academic_class_form.is_valid():
            academic_class_form.save()
            message = "Academic Class Successfully Added"
    else:
        academic_class_form = AcademicClassForm()
    
    academic_class = AcademicClass.objects.all()
    
    context = { 
        'form': academic_class_form,
        'msg': message,
        'academic_class': academic_class,
    }
    
    return render(request, "add_academic_class.html", context)



def edit_academic_class_view(request,academic_class_id):
    academic_class = AcademicClass.objects.get(id=academic_class_id)
    message = ""
    if request.method == "POST":
        academic_class_form = AcademicClassForm(request.POST,instance=academic_class)

        if academic_class_form.is_valid():
            academic_class_form.save()
            message = "Changes saved Successfully"

        else :
            message = "form has valid data"
    else:
        academic_class_form = AcademicClassForm(instance = academic_class)
    context ={
        'form':academic_class_form,
        'academic_class':academic_class,
        'message':message,
    }

    return render (request,'edit_academic_class.html',context)


def delete_academic_class_view(request, academic_class_id):
    academic_class = AcademicClass.objects.get(id=academic_class_id)
    academic_class.delete()
    return redirect('add_academic_class_page')

























