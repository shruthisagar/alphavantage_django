from django.urls import path
from alpha import views

urlpatterns = [path("quotes", views.handle_request, name="quotes")]
