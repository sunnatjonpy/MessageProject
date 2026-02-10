from django.urls import path
from .views import MessageListView, MessageCreateView, MessageDeleteView

urlpatterns = [
  path('',MessageCreateView.as_view(), name='message_new' ),
  path('messages/', MessageListView.as_view(), name='messages_list' ),
  path('messages/<int:pk>/delete', MessageDeleteView.as_view(), name='message_delete'),
]