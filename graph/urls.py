from django.urls import path
from .views import *

app_name = 'graph'

urlpatterns = [
    path('graph/',Graph.as_view(),name='graph')
]