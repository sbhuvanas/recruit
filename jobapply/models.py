from django.db import models

# Create your models here.
from django.conf import settings
from django.utils import timezone

class jobApply(models.Model):
	jobStatus = (
	    ['pending', "Pending"],
	    ['accepted', "Accepted"],
	    ['rejected', "Rejected"],
	)
	firstName = models.CharField(max_length = 20, null=True, blank=True)
	lastName = models.CharField(max_length = 20, null=True, blank=True)
	email = models.EmailField(max_length = 50,unique=True)
	potfolioWebsite = models.CharField(max_length = 50, null=True, blank=True)
	jobPosition = models.CharField(max_length = 20, null=True, blank=True)
	salaryExpectations = models.CharField(max_length = 20, null=True, blank=True)
	expectedJoining = models.DateField(auto_now=False,auto_now_add=False, null=True, blank=True)
	phone = models.CharField(max_length = 15, null=True, blank=True)
	relocation = models.CharField(max_length = 20, null=True, blank=True) 
	lastCompany = models.CharField(max_length = 20, null=True, blank=True)
	uploadResume = models.FileField(upload_to = 'profiles/', null=True, blank=True)
	comments = models.TextField(max_length = 50, null=True, blank=True)
	status = models.CharField(choices=jobStatus,max_length=10,default='pending')
	appliedDate = models.DateTimeField(default=timezone.now)

	def applied(self):
		self.appliedDate = timezone.now()
		self.save()
	def __str__(self):
		return self.email