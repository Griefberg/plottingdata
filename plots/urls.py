from django.conf.urls import url
from .views import FederalBudget


urlpatterns = [
    url(r'^federalbudget$', FederalBudget.as_view(), name='federal_budget')
]
