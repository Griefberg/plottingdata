from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse


class AboutView(TemplateView):
    template_name = 'about.html'


class ContactView(TemplateView):
    template_name = 'contact.html'


class HomeView(TemplateView):
    template_name = 'home.html'

class TestView(TemplateView):
    template_name = 'test.html'

