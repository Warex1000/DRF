"""drfsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include, re_path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from women.views import *


# router = routers.SimpleRouter()
# router.register(r'womentt', WomenViewSet)

# router = routers.DefaultRouter()   # Более расширенный с url 127.0.0.1:8000/api/v1/
# router.register(r'womentt', WomenViewSet, basename='womanss')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),   # Авторизация/аутентификация
    path('api/v1/women/', WomenAPIList.as_view()),
    path('api/v1/women/<int:pk>/', WomenAPIUpdate.as_view()),
    path('api/v1/womendelete/<int:pk>/', WomenAPIDestroy.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # path('api/v1/', include(router.urls)),  # 127.0.0.1:8000/api/v1/womentt/
    # path('api/v1/womenlist/', WomenViewSet.as_view({'get': 'list'})),
    # path('api/v1/womenlist/', WomenAPIList.as_view()),
    # path('api/v1/womenlist/', WomenAPIView.as_view()),
    # path('api/v1/womenlist/<int:pk>/', WomenViewSet.as_view({'put': 'update'})),
    # path('api/v1/womenlist/<int:pk>/', WomenAPIUpdate.as_view()),
    # path('api/v1/womenlist/<int:pk>/', WomenAPIList.as_view()),
    # path('api/v1/womenlist/<int:pk>/', WomenAPIView.as_view()),
    # path('api/v1/womendetail/<int:pk>/', WomenAPIDetailView.as_view()),
]

# https://www.youtube.com/watch?v=bITQ13XCU9Q&list=PLA0M1Bcd0w8xZA3Kl1fYmOH_MfLpiYMRs&index=15