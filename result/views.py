from django.shortcuts import render,redirect


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages



from result.forms import GuardianForm,StudentForm,SubjectForm, ClassForm
from result.forms import AcademicClassForm
from result.models import AcademicClass,Result
from result.models import Guardian,Student,Subject,Class,Grading,Exam
from result.forms import GradingForm
from result.forms import ExamForm
from result.forms import ResultForm




@login_required
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

@login_required
def add_guardian_view(request):
    message = ''
    if request.method == "POST":
        guardian_form = GuardianForm(request.POST)

        if guardian_form.is_valid():
            guardian_form.save()
            messages.success(request, "Successfully Added Guardian")
            guardian_form = GuardianForm()   
        else:
            messages.error(request, "Guardian form has errors")     
    else:
        guardian_form = GuardianForm()

    guardians = Guardian.objects.all()

    context = {
        'form': guardian_form,
        'msg': message,
        'guardians': guardians,
    }
    return render(request, "add_guardian.html", context)


@login_required
def edit_guardian_view(request, guardian_id):
    guardian = Guardian.objects.get(id=guardian_id)
    message = ""
    if request.method == "POST":
        guardian_form = GuardianForm(request.POST, instance=guardian)

        if guardian_form.is_valid():
            guardian_form.save()
            messages.success(request, "Successfully Edited Guardian")  
            return redirect(add_guardian_view)
        else:
            message = "form has valid data"
            messages.error(request, "Guardian form has errors")        
    else:
        guardian_form = GuardianForm(instance=guardian)

    context = {
        'form': guardian_form,
        'guardian': guardian,
        'message': message,
    }
    return render(request, 'edit_guardian.html', context)


@login_required
def delete_guardian_view(request, guardian_id):
    guardian = Guardian.objects.get(id=guardian_id)
    guardian.delete()
    messages.success(request, "Guardian deleted successfully")         
    return redirect('add_guardian_page')


#Student

@login_required
def add_student_view(request):
    message = ''
    if request.method == "POST":
        student_form = StudentForm(request.POST)

        if student_form.is_valid():
            student_form.save()
            message = "Student Successfully Added"
            messages.success(request, message)
            student_form = StudentForm()

               
        else:
            messages.error(request, "Student form has errors")
    else:
        student_form = StudentForm()

    students = Student.objects.all()

    context = {
        'form': student_form,
        'msg': message,
        'students': students,
    }
    return render(request, "add_student.html", context)


@login_required
def edit_student_view(request, student_id):
    student = Student.objects.get(id=student_id)
    message = ""
    if request.method == "POST":
        student_form = StudentForm(request.POST, instance=student)

        if student_form.is_valid():
            student_form.save()
            message = "Changes saved Successfully"
            messages.success(request, message)   
            return redirect(add_student_view)
        else:
            message = "Form has invalid data"
            messages.error(request, "Student form has errors")  
    else:
        student_form = StudentForm(instance=student)

    context = {
        'form': student_form,
        'student': student,
        'message': message,
    }
    return render(request, 'edit_student.html', context)


@login_required
def delete_student_view(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    messages.success(request, "Student deleted successfully")  
    return redirect('add_student_page')

#SUBJECT
@login_required
def add_subject_view(request):
    message = ''
    if request.method == "POST":
        subject_form = SubjectForm(request.POST)

        if subject_form.is_valid():
            subject_form.save()
            message = "Subject Successfully Added"
            messages.success(request, message) 
            subject_form = SubjectForm()
        else:
            messages.error(request, "Subject form has errors")  
    else:
        subject_form = SubjectForm()

    subjects = Subject.objects.all()

    context = {
        'form': subject_form,
        'msg': message,
        'subjects': subjects,
    }
    return render(request, "add_subject.html", context)


@login_required
def edit_subject_view(request, subject_id):
    subject = Subject.objects.get(id=subject_id)
    message = ""
    if request.method == "POST":
        subject_form = SubjectForm(request.POST, instance=subject)

        if subject_form.is_valid():
            subject_form.save()
            message = "Changes saved Successfully"
            messages.success(request, message)  
            return redirect(add_subject_view)
        else:
            message = "Form has invalid data"
            messages.error(request, "Subject form has errors") 
    else:
        subject_form = SubjectForm(instance=subject)

    context = {
        'form': subject_form,
        'subject': subject,
        'message': message,
    }
    return render(request, 'edit_subject.html', context)


@login_required
def delete_subject_view(request, subject_id):
    subject = Subject.objects.get(id=subject_id)
    subject.delete()
    messages.success(request, "Subject deleted successfully")  
    return redirect('add_subject_page')


#CLASS

@login_required
def add_class_view(request):
    message = ''
    if request.method == "POST":
        class_form = ClassForm(request.POST)

        if class_form.is_valid():
            class_form.save()
            message = "Class Successfully Added"
            messages.success(request, message)
            class_form = ClassForm()   
        else:
            messages.error(request, "Class form has errors")  
    else:
        class_form = ClassForm()

    class_s = Class.objects.all()

    context = {
        'form': class_form,
        'msg': message,
        'class_s': class_s,
    }
    return render(request, "add_class.html", context)


@login_required
@login_required
def edit_class_view(request, class_id):
    class_s = Class.objects.get(id=class_id)
    message = ""

    if request.method == "POST":
        class_form = ClassForm(request.POST, instance=class_s)

        if class_form.is_valid():
            class_form.save()
            message = "Changes saved Successfully"
            messages.success(request, message)   
            return redirect(add_class_view)
        else:
            message = "Form has invalid data"
            messages.error(request, "Class form has errors") 
            
    else:
        #
        class_form = ClassForm(instance=class_s)

    context = {
        'form': class_form,
        'class_s': class_s,
        'message': message,
    }
    return render(request, 'edit_class.html', context)

@login_required
def delete_class_view(request, class_id):
    class_s = Class.objects.get(id=class_id)
    class_s.delete()
    messages.success(request, "Class deleted successfully") 
    return redirect('add_class_page')



#ACADEMIC CLASS

@login_required
def add_academic_class_view(request):
    message = ''
    if request.method == "POST":
        academic_class_form = AcademicClassForm(request.POST)
        
        if academic_class_form.is_valid():
            academic_class_form.save()
            message = "Academic Class Successfully Added"
            messages.success(request, message)  
            academic_class_form = AcademicClassForm() 
        else:
            messages.error(request, "Academic Class form has errors")  
    else:
        academic_class_form = AcademicClassForm()
    
    academic_class = AcademicClass.objects.all()
    
    context = { 
        'form': academic_class_form,
        'msg': message,
        'academic_class': academic_class,
    }
    return render(request, "add_academic_class.html", context)


@login_required
def edit_academic_class_view(request, academic_class_id):
    academic_class = AcademicClass.objects.get(id=academic_class_id)
    message = ""
    if request.method == "POST":
        academic_class_form = AcademicClassForm(request.POST, instance=academic_class)

        if academic_class_form.is_valid():
            academic_class_form.save()
            message = "Changes saved Successfully"
            messages.success(request, message)   
            return redirect(add_academic_class_view)
        else:
            message = "Form has invalid data"
            messages.error(request, "Academic Class form has errors")  
    else:
        academic_class_form = AcademicClassForm(instance=academic_class)
    
    context = {
        'form': academic_class_form,
        'academic_class': academic_class,
        'message': message,
    }
    return render(request, 'edit_academic_class.html', context)


@login_required
def delete_academic_class_view(request, academic_class_id):
    academic_class = AcademicClass.objects.get(id=academic_class_id)
    academic_class.delete()
    messages.success(request, "Academic Class deleted successfully")  
    return redirect('add_academic_class_page')


# GRADING
@login_required
def add_grading_view(request):
    message = ''
    if request.method == "POST":
        grading_form = GradingForm(request.POST)
        
        if grading_form.is_valid():
            grading_form.save()
            message = "Successfully Added"
            messages.success(request, message)
            grading_form = GradingForm()   
        else:
            messages.error(request, "Grading form has errors") 
    else:
        grading_form = GradingForm()
    
    grading = Grading.objects.all()
    
    context = { 
        'form': grading_form,
        'msg': message,
        'grading': grading,
    }
    return render(request, "add_grading.html", context)


@login_required
def edit_grading_view(request, grading_id):
    grading = Grading.objects.get(id=grading_id)
    message = ""
    if request.method == "POST":
        grading_form = GradingForm(request.POST, instance=grading)

        if grading_form.is_valid():
            grading_form.save()
            message = "Changes saved Successfully"
            messages.success(request, message)   
            return redirect(add_grading_view)
        else:
            message = "Form has invalid data"
            messages.error(request, "Grading form has errors")  
    else:
        grading_form = GradingForm(instance=grading)
    
    context = {
        'form': grading_form,
        'grading': grading,
        'message': message,
    }
    return render(request, 'edit_grading.html', context)


@login_required
def delete_grading_view(request, grading_id):
    grading = Grading.objects.get(id=grading_id)
    grading.delete()
    messages.success(request, "Grading deleted successfully")  
    return redirect('add_grading_page')

# EXAM
@login_required
def add_exam_view(request):
    message = ''
    if request.method == "POST":
        exam_form = ExamForm(request.POST)
        
        if exam_form.is_valid():
            exam_form.save()
            message = "Successfully Added"
            messages.success(request, message)
            exam_form = ExamForm()  
        else:
            messages.error(request, "Exam form has errors")  
    else:
        exam_form = ExamForm()
    
    exam = Exam.objects.all()
    
    context = { 
        'form': exam_form,
        'msg': message,
        'exam': exam,
    }
    return render(request, "add_exam.html", context)


@login_required
def edit_exam_view(request, exam_id):
    exam = Exam.objects.get(id=exam_id)
    message = ""
    if request.method == "POST":
        exam_form = ExamForm(request.POST, instance=exam)

        if exam_form.is_valid():
            exam_form.save()
            message = "Changes saved Successfully"
            messages.success(request, message)   
            return redirect(add_exam_view)
        else:
            message = "Form has invalid data"
            messages.error(request, "Exam form has errors")  
    else:
        exam_form = ExamForm(instance=exam)
    
    context = {
        'form': exam_form,
        'exam': exam,
        'message': message,
    }
    return render(request, 'edit_exam.html', context)


@login_required
def delete_exam_view(request, exam_id):
    exam = Exam.objects.get(id=exam_id)
    exam.delete()
    messages.success(request, "Exam deleted successfully") 
    return redirect('add_exam_page')


# RESULT
@login_required
def add_result_view(request):
    message = ''
    if request.method == "POST":
        result_form = ResultForm(request.POST)
        
        if result_form.is_valid():
            result_form.save()
            message = "Successfully Added"
            messages.success(request, message)
            result_form = ResultForm()   
        else:
            messages.error(request, "Result form has errors")  
    else:
        result_form = ResultForm()
    
    result = Result.objects.all()
    
    context = { 
        'form': result_form,
        'msg': message,
        'result': result,
    }
    return render(request, "add_result.html", context)


@login_required
def edit_result_view(request, result_id):
    result = Result.objects.get(id=result_id)
    message = ""
    if request.method == "POST":
        result_form = ResultForm(request.POST, instance=result)

        if result_form.is_valid():
            result_form.save()
            message = "Changes saved Successfully"
            messages.success(request, message)   
            return redirect(add_result_view)
        else:
            message = "Form has invalid data"
            messages.error(request, "Result form has errors")  
    else:
        result_form = ResultForm(instance=result)
    
    context = {
        'form': result_form,
        'result': result,
        'message': message,
    }
    return render(request, 'edit_result.html', context)


@login_required
def delete_result_view(request, result_id):
    result = Result.objects.get(id=result_id)
    result.delete()
    messages.success(request, "Result deleted successfully")  
    return redirect('add_result_page')


# SIGN UP
def sign_up_view(request):
    if request.method == "POST":
        sign_up_form = UserCreationForm(request.POST)
        if sign_up_form.is_valid():
            sign_up_form.save()
            message = "User Created"
            messages.success(request, message)   
        else:
            message = "User Not Created"
            messages.error(request, message)     
    else:
        sign_up_form = UserCreationForm()
    
    context = {
        'form': sign_up_form
    }
    return render(request, 'registration/sign_up.html', context)






















