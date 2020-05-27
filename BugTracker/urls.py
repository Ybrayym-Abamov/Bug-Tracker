from django.urls import path
from BugTracker import views

urlpatterns = [
    path('', views.main, name='homepage'),
    path('logout/', views.logout_request, name='logout'),
    path('login/', views.login_request, name='login'),
    path('createticket/', views.createticket),
    path('ticketinfo/<int:ticketid>', views.ticketdetail, name="ticketdetail"),
    path('filerinfo/<int:filerid>', views.userinfo),
    path('ticketassignment/<int:ticketid>/inprogress/<int:userid>',
         views.assignticket),
    path('ticketcomplete/<int:ticketid>/complete/<int:userid>',
         views.completedticket),
    path('ticketinvalid/<int:ticketid>/invalid/<int:userid>',
         views.invalidticket),
    path('ticketedit/<int:ticketid>/edit/', views.editticket)
]
