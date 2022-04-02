from django import forms
from .models import PipelineInput


class PipelineInputForm(forms.ModelForm):

    class Meta:
        model = PipelineInput
        fields = 'name', 'pipeline'


class PipelineInformationForm(forms.Form):

    if len(PipelineInput.objects.all()):
        PIPELINE_MODELS = (
            (pipeline.name_slug, pipeline.name_slug)
            for pipeline in PipelineInput.objects.all()
        )
    else:
        PIPELINE_MODELS = ()

    print(tuple(PIPELINE_MODELS))

    EDUCATION_CHOICES = (
        ("Graduate", "Graduate"),
        ("Not Graduate", "Not Graduate")
    )

    YES_NO_CHOICES = (
        ("Yes", "Yes"),
        ("No", "No")
    )

    MALE_FEMALE_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female")
    )

    LOAN_AMOUNT_TERM = (
        (12, 12),
        (36, 36),
        (60, 60),
        (84, 84),
        (120, 120),
        (180, 180),
        (240, 240),
        (300, 300),
        (360, 360),
        (480, 480)
    )

    CREDIT_HISTORY = (
        (0, 0),
        (1, 1)
    )

    DEPENDENTS = (
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3+', '3+')
    )

    PROPERTY_AREA = (
        ("Rural", "Rural"),
        ("Semiurban", "Semiurban"),
        ("Urban", "Urban")
    )

    gender = forms.ChoiceField(choices=MALE_FEMALE_CHOICES)
    married = forms.ChoiceField(choices=YES_NO_CHOICES)
    dependents = forms.ChoiceField(choices=DEPENDENTS)
    education = forms.ChoiceField(choices=EDUCATION_CHOICES)
    self_employed = forms.ChoiceField(choices=YES_NO_CHOICES)
    applicant_income = forms.IntegerField(min_value=0)
    co_applicant_income = forms.IntegerField(min_value=0)
    loan_amount = forms.IntegerField(min_value=0)
    loan_amount_term = forms.ChoiceField(choices=LOAN_AMOUNT_TERM)
    credit_history = forms.ChoiceField(choices=CREDIT_HISTORY)
    property_area = forms.ChoiceField(choices=PROPERTY_AREA)
    pipeline = forms.ChoiceField(choices=tuple(PIPELINE_MODELS))
