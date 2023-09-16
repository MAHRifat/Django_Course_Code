from django.shortcuts import render
from first_app.forms import StudentForm
from first_app.models import Teacher,Student

# Create your views here.
def home(request):
    std = StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
    else:
        form = StudentForm()
    return render(request, 'home.html', {'form' : form})

def showData(request):
    # students list for one teacher
    teacher = Teacher.objects.get(name = 'Tarek')
    students = teacher.student.all()         # class name Student choto hat er lekhte hobe
    for stud in students:
        print(stud.name, stud.roll, stud.class_name)
    # teachers list for one student  
    stu = Student.objects.get(name = 'Rifat')
    teachers = stu.teachers.all()    # models e related_name ja dibo ta use korte hobe
    # teachers = stu.teacher_set.all()        # jekhane manytomany use kora hou oikhane class_name_set use korte hoy r class er nam chotohat er hoy
    for tec in teachers:
        print(f"{tec.name} {tec.subject} {tec.mobile_num}")
    return render(request, 'show_data.html')