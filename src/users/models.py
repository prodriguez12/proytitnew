# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
	"""docstring for CustomUser"""
	pass

	def __str__(self):
		return self.email	