"""smartcleancity URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

import users
from smartcleancityapi import views
from smartcleancityapi.views import createComplaint, createBin, assignWorkAdmin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^viewcomplaintadmin', views.ViewComplaintAdmin.as_view()),
    url(r'^viewusers', views.ViewUsers.as_view()),
    url(r'^viewcomplaintuser', views.ViewComplaintUser.as_view()),
    url(r'^viewassignedworkadmin', views.ViewAssignedWorkAdmin.as_view()),
    url(r'^viewworkdriver', views.ViewWorkDriver.as_view()),
    url(r'^getdriverlistadmin', views.GetDriverListAdmin.as_view()),
    url(r'^getbinlistadmin', views.GetBinListAdmin.as_view()),
    url(r'^createcomplaint', createComplaint),
    url(r'^createbin', createBin),
    url(r'^assignworkadmin', assignWorkAdmin),
    path('api/account', include('users.urls'))

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
