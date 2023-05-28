from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('profile', profile, name='profile'),
    path('available', available, name='available'),
    path('faq', faq, name='faq'),
    path('about', about, name='about'),
    path('match', match, name='match'),
    path('dashboard', dashboard, name='dashboard'),

]