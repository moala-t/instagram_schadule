from django.db import models
from django.utils import timezone
import pathlib
import os
# Create your models here.



class Content(models.Model):
    name = models.CharField(default="", max_length=300, blank=True)
    file = models.FileField(upload_to="media", null=True)
    is_story = models.BooleanField(default=False)
    is_post = models.BooleanField(default=False)
    schadule = models.DateTimeField(default=timezone.now)
    caption = models.TextField(default="this is caption")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-modified']
    
    def delete_with_file(self):
        os.remove(pathlib.Path(__file__).parent.parent.joinpath(str(self.file)))
        self.delete()

    def __str__(self):
        return self.name
    
