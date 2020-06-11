from django.contrib import admin
from django.urls import path
from alldata.Loginviews import login
#from alldata.Workviews import work


# This url file is for app1
urlpatterns = [
	path('',login),
	#path('',work)
]
