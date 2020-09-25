from django.urls import path
from django.contrib.auth.views import LoginView

from .views import *

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
]