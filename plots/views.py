from django.shortcuts import render
from django.views.generic import TemplateView


class FederalBudget(TemplateView):
    template_name = 'plots/federal_budget.html'

