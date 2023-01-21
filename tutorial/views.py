from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'


class AbautView(TemplateView):
    template_name = 'blog.html'


class ServiseView(TemplateView):
    template_name = 'contact.html'


class PriseView(TemplateView):
    template_name = 'portfolio.html'
    


class BlogView(TemplateView):
    template_name = 'portfolio-item.html'


class DetaillView(TemplateView):
    template_name = 'ui-elements.html'


class TeamView(TemplateView):
    template_name = 'blog-post.html'

