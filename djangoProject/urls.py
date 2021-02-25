"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
                  path('auth/', include('rest_framework.urls')),
                  path('admin_page/', include('adminPage.urls')),
                  path('constr_proj/', include('construction_project.urls')),

                  path('token', TokenObtainPairView.as_view()),
                  path('token/refresh', TokenRefreshView.as_view())
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)