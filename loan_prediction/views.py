import pickle

import pandas as pd

from django.shortcuts import render
from django.contrib import messages

from .forms import (
    PipelineInput, PipelineInputForm,
    PipelineInformationForm
)


def index(request):
    return render(request, "index.html")


def add_pipeline(request):
    message = "Add a new pipeline for making predictions"

    if request.method == 'POST':
        form = PipelineInputForm(request.POST, request.FILES)

        if form.is_valid():
            cd = form.cleaned_data

            name, pipeline = cd['name'], cd['pipeline']

            PipelineInput.objects.create(
                name=name,
                name_slug='_'.join(name.split(' ')),
                pipeline=pipeline
            ).save()

            messages.success(request, 'Pipeline Stored! Do you wish to add another?')
        else:
            messages.error(request, "Failed to store pipeline! Couldn't store pipeline")
    else:
        form = PipelineInputForm()

    context = {
        'form': form,
        'message': message,
    }

    return render(request, "loan_prediction/add_pipeline.html", context)


def check_loan_status(request):
    message = "Fill in the information before to predict the loan status"

    if request.method == 'POST':
        form = PipelineInformationForm(request.POST)

        if form.is_valid():
            OUTCOME = {
                0: "No",
                1: "Yes"
            }

            cd = form.cleaned_data

            (gender, married, dependents, education, self_employed, applicant_income, co_applicant_income,
            loan_amount, loan_amount_term, credit_history, property_area, pipeline) = (
                cd['gender'], cd['married'], cd['dependents'], cd['education'], cd['self_employed'],
                cd['applicant_income'], cd['co_applicant_income'], cd['loan_amount'], float(cd['loan_amount_term']),
                float(cd['credit_history']), cd['property_area'], cd['pipeline']
            )

            pipeline = PipelineInput.objects.get(name_slug=pipeline)

            data = [[
                gender, married, dependents, education, self_employed, applicant_income,
                co_applicant_income, loan_amount, loan_amount_term, credit_history, property_area
            ]]

            columns = [
                'Gender', 'Married', 'Dependents', 'Education', 'Self_Employed',
                'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
                'Loan_Amount_Term', 'Credit_History', 'Property_Area'
            ]

            predictor = pickle.load(open(pipeline.pipeline.path, 'rb'))

            df = pd.DataFrame(data, columns=columns)

            outcome = OUTCOME[predictor.predict(df)[0]]

            messages.success(request, f'Result! The model predicted "{outcome}"!')
        else:
            messages.error(request, "Form not valid! Couldn't predict outcome")
    else:
        form = PipelineInformationForm()

    context = {
        'form': form,
        'message': message
    }

    return render(request, "loan_prediction/check_loan_status.html", context)
