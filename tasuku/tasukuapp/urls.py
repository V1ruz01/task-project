#make pathes here
from django.urls import path

from .views import TempltView

app_name = 'tasukuapp'

urlpatterns = [
    path('', TempltView.as_view(), name='templtview'),
]