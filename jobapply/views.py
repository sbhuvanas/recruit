from django.shortcuts import render
from jobapply.models import jobApply
from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

# Create your views here.
def jobForm(request):
	if request.method == "POST":
		print request.POST
		try:
			jobApply.objects.create(firstName=request.POST['firstName'],
									lastName=request.POST['lastName'],
									potfolioWebsite=request.POST['potfolioWebsite'],
									lastCompany=request.POST['lastCompany'],
									relocation=request.POST['relocation'],
									uploadResume=request.FILES.get('uploadResume', False),
									salaryExpectations=request.POST['salaryExpectations'],
									phone=request.POST['phone'],
									comments=request.POST['comments'],
									email=request.POST['email'],
									jobPosition=request.POST['jobPosition'],
									)
			messages.success(request, 'Your Application has been submitted successfuly.')
			return render(request, 'registerjob/jobform.html', {})
		except IntegrityError:
				messages.error(request, 'Oops! There seems to be a user registered with that email address. Please try using another email address.')
				return redirect(reverse('jobapply.views.jobForm'))
	else:
		return render(request, 'registerjob/jobform.html', {})