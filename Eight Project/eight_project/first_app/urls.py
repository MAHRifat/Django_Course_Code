from django.urls import path
from first_app.views import signup,home,User_login,profile,user_logout,pass_change,pass_change_without_old_pass,ChangeUserData

urlpatterns = [
    path('', home,name="homepage"),
    path('signup/', signup, name='signup'),
    path('login/', User_login, name='login'),
    path('profile/', profile , name='profile'),
    path('logout/', user_logout , name='logout'),
    path('changeuserdata/', ChangeUserData , name='changeuserdata'),
    path('changepass/', pass_change , name='passchange'),
    path('changepass_without_old_pass/', pass_change_without_old_pass , name='passchange2'),
]
