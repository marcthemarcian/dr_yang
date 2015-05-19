from django.shortcuts import render
from django.views import generic


class IndexView(generic.TemplateView):
    template_name = "yang/index.html"


class QuestionnaireView(generic.TemplateView):
    template_name = "yang/questionnaire.html"


class AssessView(generic.TemplateView):
    template_name = "yang/assess.html"


class AboutView(generic.TemplateView):
    template_name = "yang/about.html"