from django.db import models

class Group(models.Model):
  name = models.CharField(max_length=20)
  start_time = models.TimeField()
  end_time = models.TimeField()
  created_at = models.DateTimeField(auto_now=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name