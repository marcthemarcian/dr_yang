from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import FormView
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from yang.forms import AssessmentForm
import pickle
import os

class IndexView(generic.TemplateView):
    template_name = "yang/index.html"


class QuestionnaireView(generic.TemplateView):
    template_name = "yang/questionnaire.html"


class AssessView(FormView):
    template_name = "yang/assess.html"
    form_class = AssessmentForm

    def post(self, *args, **kwargs):
        form = AssessmentForm(self.request.POST)

        if form.is_valid():
            input_array = [];
            input_array.append(self.request.POST['age']);
            input_array.append(self.request.POST['sex']);
            input_array.append(self.request.POST['chestpain']);
            input_array.append(self.request.POST['bloodpressure']);
            input_array.append(self.request.POST['cholesterol']);
            input_array.append(self.request.POST['bloodsugar']);
            input_array.append(self.request.POST['ecg']);
            input_array.append(self.request.POST['heartrate']);
            input_array.append(self.request.POST['angina']);
            input_array.append(self.request.POST['stdepression']);
            input_array.append(self.request.POST['slope']);
            input_array.append(self.request.POST['vessels']);
            input_array.append(self.request.POST['thal']);
            print input_array

            module_dir = os.path.dirname(__file__)  # get current directory
            file_path1 = os.path.join(module_dir, 'SVC_model.pkl')
            file_path2 = os.path.join(module_dir, 'scaler.pkl')

            model_pkl_file = open(file_path1, 'rb')
            scaler_pkl_file = open(file_path2, 'rb')

            model = pickle.load(model_pkl_file)
            scaler = pickle.load(scaler_pkl_file)

            scaler_pkl_file.close()
            model_pkl_file.close()

            input_array = scaler.transform(input_array)
            
            predict_proba = model.predict_proba(input_array)
            print "Prediction Probabilities", predict_proba

            prediction = model.predict(input_array)
            print "Prediction", prediction

            result = prediction # place result here
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
            context['message'] = "The patient's heart status indicates a heart problem."            
        else:
            context['message'] = "The patient's heart seems to be healthy."
        return context