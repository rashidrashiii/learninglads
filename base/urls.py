from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),

    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room"),
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),


    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<str:pk>/', views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),
    path('delete-message/<str:pk>/', views.deleteMessage, name="delete-message"),

    path('update-user/', views.updateUser, name="update-user"),

    path('topics/', views.topicsPage, name="topics"),
    path('activity/', views.activityPage, name="activity"),

    path('admin-dashboard/',views.adminDashboard, name="admin-dashboard"),
    path('admin-menu/',views.adminMenu, name="admin-menu"),
    path('users/',views.usersList, name="users"),
    path('user-search/', views.userSearch, name='user-search'),

    path('delete-user/<str:pk>/', views.deleteUser, name="delete-user"),
    path('delete-rooms/<str:pk>/', views.deleteRooms, name="delete-rooms"),
    path('report/', views.reportPage, name="report"),
    path('reports/', views.reportsPage, name="reports"),
    path('reportview/<str:pk>/', views.reportsView, name="reportview"),
    path('readed-reportview/<str:pk>/', views.readedreportsView, name="readed-reportview"),
    path('readreport',views.reportRead, name="readreport"),
    path('about/',views.about, name="about"),
    path('privacy-policy/',views.privacy, name="privacy-policy"),
    path('terms-of-service/',views.terms, name="terms-of-service"),
]
