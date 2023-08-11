from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.lobby),
    path('find-users-to-connect/', views.FindUsersToConnect.as_view(), name="find-users-to-connect"),
]
