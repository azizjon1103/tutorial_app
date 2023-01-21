from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView, name='home'),
    path('blog/', views.BlogView, name='blog'),
    path('shop/<slug:slug>', views.DetailView, name='detail'),

]

