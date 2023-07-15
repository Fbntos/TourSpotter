"""
URL configuration for TourSpotter project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from web import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path("", include('web.urls')),
    path('ciudad_detail/<int:ciudad_id>/', views.ciudad_detail, name='ciudad_detail'),
    path("chile/", views.chile, name="sobre_chile"),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("about/", views.about, name="about"),
    path("ciudades/", views.ciudades, name="ciudades"),
    path("get_all/", include('api.urls'), name="get_all"),
    path("api/", include('api.urls'), name="filter")
]
