from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy, reverse

# Create your models here.

class Message(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  phone_number = models.CharField(max_length=100)
  email = models.EmailField()
  message = models.TextField()
  creadet_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.first_name} {self.last_name}"
  
