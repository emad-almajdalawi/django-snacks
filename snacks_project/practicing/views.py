from django.shortcuts import render
from django.views.generic import TemplateView

class PracticingView (TemplateView):
    template_name = 'practicing.html'
