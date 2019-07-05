# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.core.files import File
from django.db import models

# Create your models here.
def input_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/input_<id>/<filename>
    # obtenido de https://docs.djangoproject.com/en/2.2/ref/models/fields/#field-types
   return 'input_{0}/{1}'.format(instance.user.id, filename)

class Input(models.Model):
	owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
	red_vial_layer = models.CharField(max_length = 500, null=False, blank=False)
	GPS_layer = models.CharField(max_length = 500, null=False, blank=False)
	gbd = models.FileField(blank=False, upload_to=input_directory_path)
	description = models.TextField(default='')
	gbd_root = models.CharField(max_length = 500)
	metrica = models.CharField(max_length =500, blank=False)

	def __str__(self):
		return "%s %s" % (self.GPS_layer, self.red_vial_layer)