from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home_page'),
    path('store_info/', views.Store_info.as_view(), name='store_page'),
    path('show_info/', views.show_info.as_view(),name='show_page'),
    path('delete_info/<int:pk>', views.DeleteInfo.as_view(), name= "delete_page"),
    path('update_info/<int:pk>', views.InfoUpdate.as_view(), name = "edit_page"),
    path('complete_info/<int:pk>', views.Complete.as_view(), name= "complete_page"),

]
