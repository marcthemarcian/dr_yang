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


class AssessmetForm(forms.Form):
    age = forms.IntegerField(min_value=1, required=True)
    sex = forms.ChoiceField(choices=sex_choice, widget=forms.RadioSelect(),
                            required=True)
    chestpain = forms.ChoiceField(choices=chestpain_choice,
                                  widget=forms.RadioSelect(), required=True)
    bloodpressure = forms.IntegerField(required=True)
    cholesterol = forms.IntegerField(required=True)
    bloodsugar = forms.ChoiceField(choices=yesno_choice,
                                   widget=forms.RadioSelect(), required=True)
    ecg = forms.ChoiceField(choices=ecg_choice, widget=forms.RadioSelect(),
                            required=True)
    heartrate = forms.IntegerField(required=True)
    angina = forms.ChoiceField(choices=yesno_choice,
                               widget=forms.RadioSelect(), required=True)
    stdepression = forms.IntegerField(required=True)
    slope = forms.ChoiceField(choices=slope_choices,
                              widget=forms.RadioSelect(), required=True)
    vessels = forms.IntegerField(min_value=0, max_value=3)
    thal = forms.ChoiceField(choices=thal_choice, widget=forms.RadioSelect(),
                             required=True)
