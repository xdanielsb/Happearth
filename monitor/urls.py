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
from monitor.views import (
    VStatus,
    VCommunity,
    VActions,
    VWallet,
    VCalendar,
    VMeter,
    VAssistant,
)

from django.urls import path 

app_name="monitor"

urlpatterns = [
  path('', VStatus.as_view(), name="home"),
  path('calendar/', VCalendar.as_view(), name="calendar"),
  path('community/', VCommunity.as_view(), name="community"),
  path('actions/', VActions.as_view(), name="actions"),
  path('wallet/', VWallet.as_view(), name="wallet"),
  path('meter/', VMeter.as_view(), name="meter"),
  path('assistant/', VAssistant.as_view(), name="assistant"),
]
