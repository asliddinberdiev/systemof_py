from django.db import models
from groups.models import Group
from django.core.exceptions import ValidationError
import os

def validate_phone(value):
    if not (value.isdigit() and len(value) == 12):
        raise ValidationError('Phone number must be exactly 12 digits.')

class Pupil(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    pupil_phone = models.CharField(max_length=12, unique=True, validators=[validate_phone])
    parent_phone = models.CharField(max_length=12, unique=True, validators=[validate_phone])
    image = models.ImageField(upload_to='images/', blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.firstname

    def save(self, *args, **kwargs):
        if self.pk:  # If this is an update (not a new instance)
            old_pupil = Pupil.objects.get(pk=self.pk)
            if old_pupil.image and old_pupil.image != self.image:
                # Delete old image file
                if os.path.isfile(old_pupil.image.path):
                    os.remove(old_pupil.image.path)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Delete the image file before deleting the object
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)
