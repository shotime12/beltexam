from __future__ import unicode_literals

from django.db import models
from django.contrib import messages
from  ..loginapp.models import User
# Create your models here.
class DestinationManager(models.Manager):
	def addTrip(self, request):
		is_valid = True

		if len(request.POST['name']) == 0:
 			messages.error(request, "Please enter a Destination")
			return False

		if len(request.POST['description']) == 0:
 			messages.error(request, "Please enter a Description")
			return False	

		if len(request.POST['start_date']) == 0:
 			messages.error(request, "Please enter a start date")
 			print request.POST['start_date']
			return False

		if len(request.POST['end_date']) == 0:
 			messages.error(request, "Please enter a end date")
 			print request.POST['end_date']
			return False

		if request.POST['start_date']>request.POST['end_date']:
			messages.error(request, "Please enter a valid end date")

		if not is_valid:
			return False

 		return True


class Destination(models.Model):
	name = models.CharField(max_length=255)
	start_date = models.DateField()
	end_date = models.DateField()
	plan = models.CharField(max_length=255)
	
	users = models.ManyToManyField(User, related_name = 'destinations')
	creator_user = models.ForeignKey(User)
	
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = DestinationManager()
