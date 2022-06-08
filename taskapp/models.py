from django.db import models
from django.http.response import HttpResponseRedirect
from django.urls import reverse

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=20,null=True)
    content = models.TextField()
    create_date = models.DateField(auto_now_add=True)
    status_choices = (
        ('pending', 'pending'),
        ('completed', 'completed'),
        
    )

    status = models.CharField(max_length=9,choices=status_choices,default='pending') 

    def get_absolute_url(self):
        return reverse('show-task')


    def __str__(self):
        return self.title
