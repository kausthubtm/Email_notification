from . import views
from django.urls import path


app_name = 'mysite'
urlpatterns = [
    path('login/', views.loginpage, name='login'),
    path('register/', views.registerpage, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('admin/', views.admin, name='admin'),
    path('send_email/', views.send_email, name="send_email"),
    path('home/', views.home, name='home'),
    path('forms/', views.forms, name='forms'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('add_application_form_submission/', views.add_application_form_submission,
         name='add_application_form_submission'),

    ]

