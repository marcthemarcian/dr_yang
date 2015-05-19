from django import forms

sex_choice = [(1, 'Male'), (0, 'Female')]
chestpain_choice = [(1, 'Typical Angina'), (2, 'Atypical Angina'),
                    (3, 'Non-anginal Pain'), (4, 'Asymptomatic')]
yesno_choice = [(1, 'Yes'), (2, 'No')]
ecg_choice = [(0, 'Normal'),
              (1, 'Having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)'),
              (2, 'Showing probable or definite left ventricular hypertrophy by Estes\' criteria')]
slope_choice = [(1, 'Upsloping'), (2, 'Flat'), (3, 'Downsloping')]
thal_choice = [(3, 'Normal'), (6, 'Fixed Defect'), (7, 'Reversable Defect')]


class AssessmentForm(forms.Form):
    age = forms.IntegerField(min_value=1, required=True, label='How old is the patient?')
    sex = forms.ChoiceField(choices=sex_choice, widget=forms.RadioSelect(),
                            required=True, label='What is the patient\'s sex?')
    chestpain = forms.ChoiceField(choices=chestpain_choice, widget=forms.RadioSelect(),
                                  required=True, label='What type of chest pain is the patient experiencing?')
    bloodpressure = forms.IntegerField(required=True, label='How much is the person\'s resting blood pressure (in mmHg)?')
    cholesterol = forms.IntegerField(required=True, label='How much is the patient\'s serum cholesterol (in mg/dl)?')
    bloodsugar = forms.ChoiceField(choices=yesno_choice, widget=forms.RadioSelect(),
                                   required=True, label='Does the patient have a fasting blood sugar > 120 mg/dl?')
    ecg = forms.ChoiceField(choices=ecg_choice, widget=forms.RadioSelect(),
                            required=True, label='What is the patient\'s resting electrocardiographic results?')
    heartrate = forms.IntegerField(required=True, label='How much is the patient\'s maximum achieved heart rate?')
    angina = forms.ChoiceField(choices=yesno_choice, widget=forms.RadioSelect(),
                               required=True, label='Does that patient experience exercise-induced angina?')
    stdepression = forms.IntegerField(required=True, label='What is the patient\'s ST depression induced by exercise?')
    slope = forms.ChoiceField(choices=slope_choice, widget=forms.RadioSelect(),
                              required=True, label='What is the slope of the peak exercise ST segment?')
    vessels = forms.IntegerField(min_value=0, max_value=3, label='How many major vessels does the patient have?')
    thal = forms.ChoiceField(choices=thal_choice, widget=forms.RadioSelect(),
                             required=True, label='Does the patient have a known heart defect?')
