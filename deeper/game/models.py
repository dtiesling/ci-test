from django.db import models


class Dumb_Model(models.Model):
    # comments are dumb

    title = models.CharField(max_length=255,
         help_text='fail')