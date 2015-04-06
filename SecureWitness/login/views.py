from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.core.urlresolvers import reverse
from login import forms
from login.forms import UserForm

from login.models import User
# Create your views here.

class ListUserView(ListView):

   model = User


class CreateUserView(CreateView):

   model = User
   #template_name = 'edit_user.html'
   form_class = forms.UserForm
   
   
   def get_success_url(self):
      return reverse('user-list')
      
   def get_context_data(self, **kwargs):
      
      context = super(CreateUserView, self).get_context_data(**kwargs)
      context['action'] = reverse('user-new')
      
      return context
      
      
      
class UpdateUserView(UpdateView):

   model = User
   #template_name = 'edit_user.html'
   form_class = forms.UserForm
   def get_success_url(self):
      return reverse('user-list')
      
      
   def get_context_data(self, **kwargs):
   
      context = super(UpdateUserView, self).get_context_data(**kwargs)
      context['action'] = reverse('user-edit', kwargs={'pk': self.get_object().id})
      
      return context
      
      
class DeleteUserView(DeleteView):

   model = User
   #template_name = 'delete_user.html'
   
   def get_success_url(self):
      return reverse('user-list')
      
      
class UserView(DetailView):
   model = User