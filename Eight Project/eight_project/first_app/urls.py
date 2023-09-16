from django.urls import path
from first_app.views import signup,home,User_login,profile,user_logout

urlpatterns = [
    path('', home,name="homepage"),
    path('signup/', signup, name='signup'),
    path('login/', User_login, name='login'),
    path('profile/', profile , name='profile'),
    path('logout/', user_logout , name='logout'),
]
