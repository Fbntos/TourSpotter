from django.urls import path
from api import views

urlpatterns = [
    path('', views.get_all, name=''),
    path("filter&name=<str:name>/", views.filter, name="filter")
]