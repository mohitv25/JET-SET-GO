from django.contrib import admin
from django.urls import path, include
from travel import views
urlpatterns = [
    path('', views.home  ,name='main'),
    path('about/',views.about  ,name='about'),
    path('blog/',views.blog  ,name='blog'),
    path('contact/',views.Contact ,name='contact'),
    path('portfolio/',views.portfolio  ,name='portfolio'),
    path('services/',views.services ,name='services'),
    path('team/',views.team  ,name='team'),
    path('planner/', views.itinerary_planner, name='itinerary_planner'),
    path('countries/',views.tourist_location_by_country,name = 'countries'),
    path('group/',views.group_booking_management, name= 'group'),
    path('status', views.itinerary_status, name='itinerary_status'),
     path('group_booking/', views.group_booking, name='group_booking')

]
