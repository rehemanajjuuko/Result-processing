from django.forms import ModelForm
from result.models import Guardian 
from result.models import Student,Subject, Class,AcademicClass
from result.models import Grading ,Exam ,Result

class GuardianForm (ModelForm):
    class Meta:
        model = Guardian
        fields = '__all__'
class StudentForm (ModelForm):
    class Meta:
        model = Student
        fields ='__all__'

class SubjectForm(ModelForm):
    class Meta:
        model= Subject
        fields = '__all__'

class ClassForm (ModelForm):
    class Meta:
        model = Class
        fields = "__all__"

class AcademicClassForm(ModelForm):
    class Meta:
        model = AcademicClass
        fields = "__all__"

class GradingForm(ModelForm):
    class Meta:
        model = Grading
        fields = "__all__"

class ExamForm (ModelForm):
    class Meta:
        model = Exam
        fields = "__all__"
class ResultForm (ModelForm):
    class Meta:
        model = Result
        fields = "__all__"

