from django.urls import path
from portfolio.views import * 

app_name='portfolio'

urlpatterns=[
    path('',portfolio_view,name='portfolio'),
    path('<int:pid>',portfolio_details_view,name='portfolio-details'),
]