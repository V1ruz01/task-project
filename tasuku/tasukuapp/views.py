from django.shortcuts import render
from django.views.generic import TemplateView
from .models import TaskStatus

# Create your views here.

# must be CBV!
# it has models, template shows (template_{path}), context_object_name
class TempltView(TemplateView):
    model = TaskStatus
    template_name = 'tasks/base.html'
    context_object_name = 'tasks/base.html'