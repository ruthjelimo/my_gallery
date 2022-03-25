from django.urls import path
from . import views

urlpatterns=[
    path('',views.welcome,name = 'welcome'),
    path('today/',views.album_of_day,name='albumToday')
]