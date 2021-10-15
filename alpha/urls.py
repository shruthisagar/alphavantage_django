from django.urls import path
from alpha import views

urlpatterns = [
    path("/", views.handle_request)
]