from django.urls import path
from . import views

urlpatterns = [
    path('films/', views.FilmAPIView.as_view()),
    path('tickets/', views.TicketAPIView.as_view()),
    path('halls/', views.HallAPIView.as_view()),
    path('shows/', views.ShowAPIView.as_view()),
    path('users/', views.UserAPIView.as_view()),
    path('auth/', views.CustomerAuthAPIView.as_view()),
    path('seats/', views.SeatAPIView.as_view()),
]