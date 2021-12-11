from django.urls import path
from . import views

urlpatterns = [
	path('geo-detail/<str:pk>/', views.geoDetail, name="geo-detail"),
	path('geo-create/', views.geoCreate, name="geo-create"),
	path('geo-delete/<str:pk>/', views.geoDelete, name="geo-delete"),

]