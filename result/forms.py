from django.forms import ModelForm
from result.models import Guardian
from result.models import Student,Subject, Class,AcademicClass

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