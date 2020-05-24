from django.urls import path
from BugTracker import views

urlpatterns = [
    path('', views.main, name='homepage'),
    path('logout/', views.logout_request, name='logout'),
    path('login/', views.login_request, name='login')
]
