from django.urls import path
from BugTracker import views

urlpatterns = [
    path('', views.main, name='homepage')
]
