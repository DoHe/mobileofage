from django.db import models


class Comic(models.Model):
    id = models.CharField(max_length=300, primary_key=True)
    image = models.URLField(max_length=300, null=False, blank=False)
    alt = models.URLField(max_length=300, null=False, blank=True)
    title = models.URLField(max_length=300, null=False, blank=True)
    previous = models.CharField(max_length=300, null=False, blank=False)
    next = models.CharField(max_length=300, null=True)
    date = models.CharField(max_length=10, null=False,
                            blank=False, unique=True)
