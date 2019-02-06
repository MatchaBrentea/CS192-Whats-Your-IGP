from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class ORG(models.Model):
	name = models.CharField(max_length=100, unique=True)
	desc = models.TextField()

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('app-orgs')

class IGP(models.Model):
	item = models.CharField(max_length=100)
	org = models.ForeignKey(ORG, on_delete=models.CASCADE)
	itype = models.CharField(max_length=100)
	price = models.FloatField(null=True, blank=True, default=None)
	date_posted = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.item

	def get_absolute_url(self):
		return reverse('app-igps')