from django.db import models
from picklefield.fields import PickledObjectField


class PipelineInput(models.Model):
    name = models.CharField(max_length=180)
    name_slug = models.SlugField(max_length=900)
    pipeline = models.FileField(upload_to='pipeline/')

    objects = models.Manager()

    def get_slug(self):
        return self.name_slug

    def __str__(self):
        return self.name_slug
