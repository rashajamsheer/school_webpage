from django.db import models
from django.urls import reverse


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=250, unique=True)
    wikipedia_url = models.URLField(blank=True, null=True)
    class Meta:
        ordering=('name',)
        verbose_name = 'department'
        verbose_name_plural = 'departments'

    def __str__(self):
        return '{}'.format(self.name)

class Course(models.Model):
    name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.name)

class Material(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=255)
    dob = models.DateField()
    age = models.IntegerField()
    GENDER_CHOICES = [
        ('Male', 'Male'),('Female', 'Female'),('Other', 'Other'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    purpose = models.CharField(max_length=255, choices=[('Enquiry', 'Enquiry'), ('Place Order', 'Place Order'), ('Return', 'Return')])
    materials_provide = models.ManyToManyField(Material)

    def __str__(self):
        return self.name


