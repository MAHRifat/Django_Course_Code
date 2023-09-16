from django.contrib import admin
from first_app.models import StudentModel,StudentInfoModel,TeacherInfoModel,EmployeeModel,ManagerModel,Friend,Me,Person,Passport,Post

# Register your models here.
# admin.site.register(StudentModel)
# admin.site.register(StudentInfoModel)
# admin.site.register(TeacherInfoModel)
# admin.site.register(EmployeeModel)
# admin.site.register(ManagerModel)

# @admin.register(EmployeeModel)
# class EmployeeModelAdmin(admin.ModelAdmin):
#     list_display = ['id','name','city','designation']
# @admin.register(ManagerModel)
# class ManagerModelAdmin(admin.ModelAdmin):
#     list_display = ['id','name','city','designation','take_interview','hiring']
# @admin.register(Friend)
# class FriendAdmin(admin.ModelAdmin):
#     list_display = ['id','school','section','attendence','hw']
    
# @admin.register(Me)
# class MeAdmin(admin.ModelAdmin):
#     list_display = ['id','school','section','attendence','hw']


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['id','name','city','email']
    
# @admin.register(Passport)
# class PassportAdmin(admin.ModelAdmin):
#     list_display = ['id','user','pass_number','page','validity']
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['user','post_cap','post_details']