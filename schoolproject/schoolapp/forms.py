
from django import forms
from .models import Department, Material, Student, Course


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','dob','age','gender','phone_number','email','address','department','course','purpose','materials_provide']

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['materials_provide'].widget = forms.CheckboxSelectMultiple()
        self.fields['materials_provide'].queryset = Material.objects.all()
        self.fields['course'].queryset = Course.objects.all()
        self.fields['gender'].widget = forms.RadioSelect(choices=Student.GENDER_CHOICES)
        self.fields['dob'].widget = forms.DateInput(attrs={'type': 'date'})