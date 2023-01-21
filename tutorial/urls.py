from django.urls import path
from .views import HomePageView, AbautView, ServiseView, PriseView, BlogView, DetaillView, TeamView


urlpatterns = [
    path('home/', HomePageView.as_view(), name = 'home'),
    path('about/', AbautView.as_view(), name = 'about'),
    path('servise/', ServiseView.as_view(), name = 'servise'),
    path('prise/', PriseView.as_view(), name = 'prise'),
    path('blok/', BlogView.as_view(), name = 'blok'),
    path('dedail/', DetaillView.as_view(), name = 'dedail'),
    path('deam/', TeamView.as_view(), name = 'deam' ),
]
