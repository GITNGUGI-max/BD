"""bbapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from bloodbank import views
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static


router=DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'donors', views.DonorViewSet)
router.register(r'counties', views.CountyViewSet)
router.register(r'sub_counties', views.SubCountyViewSet)
router.register(r'patients', views.PatientViewSet)
router.register(r'messages', views.MessageViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bloodbank.urls')),
 	path('auth/', include('rest_auth.urls')),
    path('auth/signup/', include('rest_auth.registration.urls')),
    path('auth/refresh-token/', refresh_jwt_token),
    path('api/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)