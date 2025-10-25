from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models

# Create your views here.

# must be CBV!
# it has models, template shows (template_{path}), context_object_name

class TaskListView(ListView):
   model = models.TaskStatus
   context_object_name = "tasks"
   template_name = "tasks/task_list.html"


class TaskDetailView(LoginRequiredMixin, DetailView):
   model = models.TaskStatus
   context_object_name = "task"
   template_name = 'tasks/task_detail.html'


class TaskCreateView(LoginRequiredMixin, CreateView):
   model = models.TaskStatus
   #form_class = TaskForm
   template_name = "tasks/task_form.html"
   success_url = reverse_lazy("tasks:task_list")

   def form_valid(self, form):
       form.instance.creator = self.request.user
       return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
   model = models.TaskStatus
   #form_class = TaskForm
   template_name = "tasks/task_update_form.html"
   success_url = reverse_lazy("tasks:task-list")


class TaskDeleteView(LoginRequiredMixin, DeleteView):
   model = models.TaskStatus
   success_url = reverse_lazy("tasks:task-list")
   template_name = "tasks/task_delete_confirmation.html"


# class CustomLoginView(LoginView):
#    template_name = "tasks/login.html"
#    redirect_authenticated_user = True


# class CustomLogoutView(LogoutView):
#    next_page = "tasks:login"


class RegisterView(CreateView):
   template_name = "registration/register.html"
   form_class = UserCreationForm

   def form_valid(self, form):
      user = form.save()
      login(self.request, user)
      return redirect(reverse_lazy("tasks:login"))