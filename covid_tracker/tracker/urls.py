from django.contrib import admin
from django.urls import path , include
from . views import IndiaTrackerView,DonateView,LatestCaseView,Essentials_ResourcesView,DeathView,HelpView

urlpatterns = [
    path('',IndiaTrackerView.as_view(),name="india"),
    path('donate',DonateView.as_view(),name="donate"),
    path('latestcases',LatestCaseView.as_view(),name="latest_cases"),
    path('essentialsresources',Essentials_ResourcesView.as_view(),name="essentials_resources"),
    path('deaths',DeathView.as_view(),name="deaths"),
    path('help',HelpView.as_view(),name="help"),
    
]


