from django.urls import path,include
from .views import WorkView, HomePageView, AboutPageView
from django.views.generic.base import RedirectView



appname="templateManager"

urlpatterns = [
    path('', RedirectView.as_view(url='/home/'), name='home'),
    path("home/",HomePageView.as_view(),name = 'home'),
    path("about/",AboutPageView.as_view(),name = 'about'),
    path("Service",WorkView.as_view(),name = 'work'),
    path("<slug:slug2>/",WorkView.as_view(),name = 'work'),
]