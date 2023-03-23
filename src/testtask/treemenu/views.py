from django.shortcuts import render
from django.views.generic import TemplateView


class IndexPageView(TemplateView):
    template_name = "treemenu/index.html"
# Create your views here.
