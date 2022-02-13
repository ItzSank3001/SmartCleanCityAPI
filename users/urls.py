from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from smartcleancityapi import views
from smartcleancityapi.views import createComplaint, createBin, assignWorkAdmin
from users.views import CustomAuthToken, logout_user, registration_view

urlpatterns = [
    url('login/', CustomAuthToken.as_view()),
    url('logout/', logout_user),
    url('signup/', registration_view),

]


