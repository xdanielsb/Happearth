"""energy_monitor_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from monitor.views import HomePage 
from monitor.views import VLanding

urlpatterns = [
  path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
  path('sadmin/', admin.site.urls),
  path('monitor/', include("monitor.urls", namespace="monitor")),
  path('account/', include("accounts.urls", namespace="account")),
  path('houses/', include("house.urls", namespace="house")),
  path('home-admin/', HomePage.as_view(), name="homepage"),
  path('', VLanding.as_view(), name="landing"),
]

admin.site.site_header = 'Energy Admin'
admin.site.site_title = 'Admin'
handler404 = 'accounts.views.handler404'
handler500 = 'accounts.views.handler500'
