
from django.shortcuts import render, redirect
import requests
from django.http import HttpResponse
from .models import Resource
from .models import Contact
from django.forms import ModelForm
from django import forms

class ContactForm(forms.ModelForm):
	class Meta:
		model=Contact
		fields=['name', 'email', 'subject', 'message' ]
		widgets={
			'name': forms.TextInput(attrs={'class':'name, form-control', 'placeholder': ' Your Name',}),
			'email': forms.EmailInput(attrs={'class':'email, form-control', 'placeholder': ' Your Email',}),
			'subject': forms.TextInput(attrs={'class':'subject, form-control', 'placeholder': ' Subject',}),
			'message': forms.Textarea(attrs={'class':'message, form-control', 'placeholder': ' Message',}),
		}


def homepage(request):
	context = {
		"active_tab": "home",
	}
	return render(request, "pages/index.html", context)

def view_resources(request): 
	resources_qs = Resource.objects.all() 
	context = {
		"resources": resources_qs,
		"active_tab": "resources", 
	}
	return render(request, "pages/resources.html", context)

def github(request):
	response = requests.get('https://api.github.com/users/gilliantrethewey/repos')
	repos = response.json()
	context = {
		"active_tab": "github",
		"github_repos": repos, 
	}
	return render(request, "pages/github.html", context)

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form = ContactForm()

	context = {
		"form": form,
		"active_tab": "contact",
	}
	return render(request, "pages/contact.html", context)

def about(request):
	context = {
		"active_tab": "about", 
	}
	return render(request, "pages/about.html", context)

def blog_archive(request):
	context = {
		"active_tab": "blog_archive", 
	}
	return render(request, "pages/blog-archive.html", context)

def portfolio(request):
	context = {
		"active_tab": "portfolio", 
	}
	return render(request, "pages/portfolio.html", context)

def resume(request):
	context = {
		"active_tab": "resume", 
	}
	return render(request, "pages/resume.html", context)

def services(request):
	context = {
		"active_tab": "services", 
	}
	return render(request, "pages/services.html", context)

def blog_post_first(request):
	context = {
		"active_tab": "blog", 
	}
	return render(request, "pages/blog-post-first.html", context)

def portfolio_details_client_grid(request):
	context = {
		"active_tab": "portfolio", 
	}
	return render(request, "pages/portfolio-details-client-grid.html", context)

def portfolio_details_feast_and_west(request): 
	context = {
		"active_tab": "portfolio", 
	}
	return render(request, "pages/portfolio-details-feast-and-west.html", context)

def portfolio_details_github(request): 
	context = {
		"active_tab": "portfolio", 
	}
	return render(request, "pages/portfolio-details-github.html", context)

def portfolio_details_kickstart_coding_data_project_2(request):
	context = {
		"active_tab": "portfolio", 
	}
	return render(request, "pages/portfolio-details-kickstart-coding-data-project-2.html", context)

def portfolio_details_kickstart_coding_data_project_3(request):
	context = {
		"active_tab": "portfolio", 
	}
	return render(request, "pages/portfolio-details-kickstart-coding-data-project-3.html", context)

def portfolio_details_peach_and_pine(request):
	context = {
		"active_tab": "portfolio", 
	}
	return render(request, "pages/portfolio-details-peach-and-pine.html", context)

def portfolio_details_rachel_anzalone(request):
	context = {
		"active_tab": "portfolio", 
	}
	return render(request, "pages/portfolio-details-rachel-anzalone.html", context)

def portfolio_details_shayla_boyd_gill(request): 
	context = {
		"active_tab": "portfolio", 
	}
	return render(request, "pages/portfolio-details-shayla-boyd-gill.html", context)

def portfolio_details_west_trade(request): 
	context = {
		"active_tab": "portfolio", 
	}
	return render(request, "pages/portfolio-details-west-trade.html", context)

