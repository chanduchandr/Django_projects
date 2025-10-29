"""
URL configuration for MyProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from customerjobcard import views
from users.views import UserViewSet, RoleViewSet, UserRoleMapViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'userrolemaps', UserRoleMapViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('jobcards/', include([
        path('', views.jobcard_list, name='jobcard_list'),
        path('create/', views.create_jobcard, name='create_jobcard'),
        path('update/<uuid:pk>/', views.update_jobcard, name='update_jobcard'),
        path('delete/<uuid:pk>/', views.delete_jobcard, name='delete_jobcard'),
    ])),

    # Optional: redirect / to /jobcards/
    path('', views.jobcard_list, name='home'),
    path('api/', include(router.urls)),
]
