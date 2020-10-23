from django.urls import path
from account.api.views import (
    registration_view
)

app_name = 'blog'

urlpatterns = [
    path('register', registration_view, name='register'),
]