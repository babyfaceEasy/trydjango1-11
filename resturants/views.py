import random
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# function based view

def home(request):
	num = random.randint(0, 100000)
	names_list = ["olakunle", "odegbaro", "lamiju", "Awofadeju", "Veronica"]
	context = {
		"bool_item": True,
		"num": num,
		"names_list" : names_list
		}
	return render(request, "home.html", context)

