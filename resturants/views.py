import random
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

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

def about_us(request):
	return render(request, "about-us.html", {})

def contact(request):
	return render(request, "contact.html", {})

class HomeView(TemplateView):
	template_name = 'home.html'

	def get_context_data(self, *args, **kwargs):
		context = super(HomeView, self).get_context_data(*args, **kwargs)
		num = random.randint(0, 100000)
		names_list = ["olakunle", "odegbaro", "lamiju", "Awofadeju", "Veronica"]
		context = {
			"bool_item": True,
			"num": num,
			"names_list" : names_list
		}
		return context

class AboutView(TemplateView):
	template_name = 'about-us.html'

class ContactView(TemplateView):
	template_name = 'contact.html'
