"""join_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from scrum import views

router = routers.DefaultRouter()
router.register(r"tasks", views.TaskViewSet)
router.register(r"users", views.UserViewSet)
router.register(r"priorities", views.PriorityViewSet)
router.register(r"categories", views.CategoryViewSet)
router.register(r"status", views.StatusViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("", include(router.urls)),
    path("register/", views.RegisterUserAPIView.as_view()),
]
