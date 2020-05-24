from django.urls import path
from BugTracker import views

urlpatterns = [
    path('', views.main, name='homepage'),
    path('logout/', views.logout_request, name='logout'),
    path('login/', views.login_request, name='login'),
    path('createticket/<int:filerid>', views.createticket),
    path('ticketinfo/<int:ticketid>', views.ticketdetail, name="ticketdetail"),
    path('userinfo/<int:userid>', views.userinfo)
]
