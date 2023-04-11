from . import views
from django.urls import path
from .views import Notes

urlpatterns = [
  path('signup/',views.signUp,name='signup'),

  path('user_login/',views.user_login,name='login'),
  path('profile/',views.profile,name='profile'),
  path('user_list/',views.user_list,name='user_list'),
  path('verifyToken/',views.verify_token,name='verify_token'),


  # admin urls
  path('admin_login/',views.admin_login,name='admin_login'),
  path('create_user/',views.create_user,name='create_user'),
  path('admineditUser/<int:id>',views.edit_user,name='edit_user'),
  path('admineditUser/<int:id>',views.edit_user,name='edit_user'),
  path('updateUser/<int:id>',views.update_user,name='edit_user'),
  path('deleteUser/<int:id>/',views.delete_user,name='deleteUser'),
  path('notes/',Notes.as_view(),name='notes'),
  path('user-update/<int:pk>/', views.userDetails, name='user-update'),
  path('user-update-form/<int:pk>/', views.userUpdate, name='user-update-form'),
  
]