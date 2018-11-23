from django.shortcuts import render

from login.models import user_data
# Create your views here.


def login(request):
	if request.method=="GET":
		return render(request,"registration.html",{})
	
	if request.method=="POST":
		first_name=request.POST.get("first_name")
		second_name=request.POST.get("second_name")
		mobile=request.POST.get("mobile")
		email=request.POST.get("email")
		password=request.POST.get("password")

		user_list= user_data.objects.get(mobile=mobile)
		for data in user_list:
			if(data.mobile==mobile)

