from django.db import models
import os

class Group(models.Model):
    name = models.CharField(max_length=20)
    start_time = models.TimeField()
    end_time = models.TimeField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        # Import Pupil here to avoid circular import issues
        from pupils.models import Pupil
        # Delete all pupil images related to this group
        pupils = Pupil.objects.filter(group=self)
        for pupil in pupils:
            if pupil.image:
                try:
                    if os.path.isfile(pupil.image.path):
                        os.remove(pupil.image.path)
                except Exception as e:
                    print(f"Error deleting file {pupil.image.path}: {e}")
        super().delete(*args, **kwargs)
