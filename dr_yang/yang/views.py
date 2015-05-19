from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import FormView
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from yang.forms import AssessmentForm

class IndexView(generic.TemplateView):
    template_name = "yang/index.html"


class QuestionnaireView(generic.TemplateView):
    template_name = "yang/questionnaire.html"


class AssessView(FormView):
    template_name = "yang/assess.html"
    form_class = AssessmentForm

    def post(self, *args, **kwargs):
        form = AssessmentForm(self.request.POST)

        print self.request.POST # naa diri sud ang 13 vars

        if form.is_valid():

            # do prediction here

            result = 1 # place result here
            self.request.session['result'] = result
            return HttpResponseRedirect(reverse('result'))
        else:
            return self.form_invalid(form)

class AboutView(generic.TemplateView):
    template_name = "yang/about.html"


class ResultsView(generic.TemplateView):
    template_name = 'yang/results.html'

    def get_context_data(self, **kwargs):
        context = super(ResultsView, self).get_context_data(**kwargs)
        context['result'] = self.request.session['result'] 


        if context['result']:
            context['message'] = "The patient's heart status is indicating a presence of a heart problem."            
        else:
            context['message'] = "The patient's heart seems to be healthy."
        return context