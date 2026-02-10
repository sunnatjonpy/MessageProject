from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView
from .models import Message


class MessageListView(ListView):
  model = Message
  template_name = 'messages_list.html'

class MessageCreateView(CreateView):
  model = Message
  fields = ('first_name','last_name','phone_number','email','message')
  template_name = 'message_new.html'

  success_url = reverse_lazy('messages_list')

class MessageDeleteView(DeleteView):
  model = Message
  template_name = 'message_delete.html'
  success_url = reverse_lazy('messages_list')


