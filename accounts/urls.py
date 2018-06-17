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
from django.urls import path 
from django.contrib.auth.views import login, logout
from accounts.views import SearchView, signup

app_name="accounts"

urlpatterns = [
  path('login/', login, {'template_name': 'accounts/login.html', 'redirect_authenticated_user': True}, name="login"),
  path('logout/', logout, {'next_page': '/'}, name="logout"),
  path('search/', SearchView.as_view(), name="search"),
  path('signup/', signup, name="signup"),
]

