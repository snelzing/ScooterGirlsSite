"""scooter_site URL Configuration

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
from django.urls import path
from main.views import HomePageView, DeviceWorkView, AccountMgmtView, TutoringView, WebsiteWorkView, ContactView, ThanksPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", HomePageView.as_view(), name="home"),
    path("troubleshooting/", DeviceWorkView.as_view(), name="troubleshooting"),
    path("account-management/", AccountMgmtView.as_view(), name="account-management"),
    path("tutoring/", TutoringView.as_view(), name="tutoring"),
    path("website-work/", WebsiteWorkView.as_view(), name="website-work"),
    path("contact/", ContactView.as_view(), name="contact"),
    path('thanks/', ThanksPageView.as_view(), name="thanks"),

]
