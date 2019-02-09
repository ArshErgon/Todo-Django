"""todopro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import handler404
from todoapp import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('d/<int:pk>/', views.delete_todo, name='delete'),
    path('sign/', views.sign_page, name='sign'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('thank/', views.thank_you_page, name="thank"),
    path('try/', views.try_page, name='try'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "todoapp.views.error_404"