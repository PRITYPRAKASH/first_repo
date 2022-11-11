from django.db import models

# Create your models here.
from django.http import*

# Create your models here.
class csvs(models.Model):
    file_name=models.FileField(upload_to="csvs")
    uploaded=models.DateTimeField(auto_now_add=True)
    activated=models.BooleanField(default='False')

    def __str__(self) :
          return f"file id: {self.id}"