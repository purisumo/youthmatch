from django.urls import path
from .views import *

urlpatterns = [
    path('', landing, name='landing'),
    path('home', home, name='home'),
    path('profile', profile, name='profile'),
    path('profile/update/', update_profile, name='update_profile'),
    path('available', available, name='available'),
    path('faq', faq, name='faq'),
    path('about', about, name='about'),
    path('match', match, name='match'),
    path('dashboard', dashboard, name='dashboard'),
    path('dashboard/user', userdash, name='userdashboard'),
    path('dashboard/job', jobdash, name='jobdashboard'),
    path('dashboard/addjob', addjob, name='addjob'),
    path('dashboard/deletejob/<str:pk>/', deletejob, name='deletejob'),
    path('dashboard/updatejob/<str:pk>/', updatejob.as_view(), name='updatejob'),
    path('job/<str:name>/', job, name='job')
]