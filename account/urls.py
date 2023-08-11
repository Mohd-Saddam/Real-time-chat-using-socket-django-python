from .views import *
from django.urls import path

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('update-interests/', UpdateUserInterest.as_view()),
    path('update-status/', UpdateUserActiveStatus.as_view()),
]
