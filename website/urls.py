from django.urls import path
from website.views import *

app_name='website'

urlpatterns=[
    path('',index_view,name='index'),
    path('contact',contact_view,name='contact'),
    path('team',team_view,name='team'),
    path('newsletter',newsletter_view,name='newsletter')
]