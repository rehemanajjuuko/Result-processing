from django.db import models

class Class (models.Model):
    class_s = models.CharField(max_length=20,verbose_name="Class Name")
    class_short_form= models.CharField(max_length=3, verbose_name="Class")
    def __str__(self):
        return f"{self.class_short_form}"

class Subject (models.Model):
    subject = models.CharField (max_length=1, verbose_name="Subject Name")
    subject_short_form = models.CharField(max_length=5,verbose_name="SUBJECT")
    def __str__(self):
        return f"{self.subject_short_form}"

class Student(models.Model):
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female')]

    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    other_name = models.CharField(max_length=30, blank=True, null=True ,default="N/A")
    date_of_birth = models.DateField()
    address = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    class_s = models.ForeignKey(Class, on_delete=models.CASCADE, verbose_name="Class")

    def __str__(self):
        return f"{self.first_name} {self.second_name} {self.class_s}"
    

class Guardian(models.Model):
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female')]
    RELATIONSHIP_CHOICES =[('M','Mother'),('F','Father'),('G','Guardian')]

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    contact = models.CharField(max_length=15)
    relationship = models.CharField(max_length=1,choices=RELATIONSHIP_CHOICES)

    def __str__(self):
        return f"{self.first_name} ({self.relationship}) {self.student}"
    


class AcademicClass(models.Model):
    TERM_CHOICES = [('1', 'Term 1'), ('2', 'Term 2'), ('3', 'Term 3')]
    STATUS_CHOICES = [('O','OPEN FOR REGISTRATION'),('C','CLOSED')]

    term = models.CharField(max_length=1, choices=TERM_CHOICES)
    year = models.IntegerField()
    class_s = models.ForeignKey(Class, on_delete=models.CASCADE)
    status = models.CharField(max_length=20 ,choices=STATUS_CHOICES)

    def __str__(self):
        return f" {self.class_s} {self.year}--{self.term}"
    

class Exam(models.Model):
    EXAM_TYPE_CHOICES = [('MOT', 'Mid term'), ('BOT', 'BEGINNING OF TERM'),
                         ('EOT','END OF TERM')]
   
    exam_date = models.DateField(auto_now=False)
    academic_class = models.ForeignKey(AcademicClass,on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    exam_type = models.CharField(max_length=10, choices=EXAM_TYPE_CHOICES)
    status = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.subject} - {self.exam_type} -{self.academic_class}"
    

class Grading(models.Model):
    points = models.IntegerField()
    max_score = models.IntegerField()
    min_score = models.IntegerField()
    grade = models.CharField(max_length=2)

    def __str__(self):
        return self.grade
    

class Result(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    score = models.IntegerField()
    grade = models.ForeignKey(Grading, on_delete=models.SET_NULL, null=True)
    remarks = models.TextField(blank=True)

    def __str__(self):
        return f"{self.student} - {self.exam} ({self.score}-{self.exam.academic_class})"
    

# Create your models here.