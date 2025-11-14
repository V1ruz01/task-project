from django.shortcuts import get_object_or_404, redirect
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView

from . import models
from .forms import TaskForm, FiltrationForm
from .mixins import UserIsOwnerMixin

# Create your views here.

# must be CBV!
# it has models, template shows (template_{path}), context_object_name

class TaskListView(ListView):
   model = models.TaskStatus
   context_object_name = "tasks"
   template_name = "tasks/task_list.html"

   def query_set(self):
      query_set = models.TaskStatus.object.all()

      if self.request.user.is_authenticated():
         query_set = query_set.filter(creator = self.request.user)

      form = FiltrationForm(self.request.GET)
      if form.is_valid():
         status = form.cleaned_data.get('status') #thinking...

      if status:
         query_set = query_set.filter(status=status)
      
      return query_set

      
class TaskDetailView(LoginRequiredMixin, DetailView):
   model = models.TaskStatus
   context_object_name = "task"
   template_name = 'tasks/task_detail.html'


class TaskCreateView(LoginRequiredMixin, CreateView):
   model = models.TaskStatus
   form_class = TaskForm
   template_name = "tasks/task_form.html"
   success_url = reverse_lazy("tasks:task_list")

   def form_valid(self, form):
       form.instance.creator = self.request.user
       return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
   model = models.TaskStatus
   form_class = TaskForm
   template_name = "tasks/task_form.html"
   success_url = reverse_lazy("tasks:task_list")


class TaskDeleteView(LoginRequiredMixin, UserIsOwnerMixin, DeleteView):
   model = models.TaskStatus
   success_url = reverse_lazy("tasks:task_list")
   template_name = "tasks/task_confirm_delete.html"


# class CustomLoginView(LoginView):
#    template_name = "tasks/login.html"
#    redirect_authenticated_user = True


# class CustomLogoutView(LogoutView):
#    next_page = "tasks:login"


class RegisterView(CreateView):
   template_name = "registration/register.html"
   form_class = UserCreationForm
   success_url = reverse_lazy("registration:login")

   def form_valid(self, form):
      response = super().form_valid(form)
      login(self.request, self.object)
      return response
   

class CommentUpdateView(LoginRequiredMixin, UpdateView):
   model = models.CommentModel
   fields = ['content']
   template_name = 'tasks/edit_comment.html'


   def form_valid(self, form):
       comment = self.get_object()
       if comment.author != self.request.user:
           raise PermissionDenied("You cant edit this comment, bro.")
       return super().form_valid(form)


   def get_success_url(self):
       return reverse_lazy('tasks:task_detail', kwargs={'pk': self.object.task.pk})


class CommentDeleteView(LoginRequiredMixin, DeleteView):
   model = models.CommentModel
   template_name = 'tasks/delete_comment.html'


   def get_queryset(self):
       queryset = super().get_queryset()
       return queryset.filter(author=self.request.user)


   def get_success_url(self):
       return reverse_lazy('tasks:task_detail', kwargs={'pk': self.object.task.pk})
   