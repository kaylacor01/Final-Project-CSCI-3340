from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import FoodResource



def home(request):
	return render(request, 'home.html',{})

def register(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, "Account created successfully")
			return redirect ("login")
	else:
		form = UserCreationForm()

	return render(request, "register.html", {"form":form})


def resource_map(request):
	resource_type = request.GET.get('type')
	if resource_type:
		resources = FoodResource.objects.filter(resource_type=resource_type)
	else:
		resources = FoodResource.objects.all()

	context = {
	'resources':resources,
	}
	return render(request, 'resources/map.html', context)
