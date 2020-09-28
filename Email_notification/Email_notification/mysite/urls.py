from . import views
from django.urls import path


app_name = 'mysite'
urlpatterns = [
    path('home/', views.home, name='home'),
    ]

