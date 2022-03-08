
from django.shortcuts import render, redirect
import requests
from django.http import HttpResponse


# Create your views here.

def homepage(request):
	context = {
		"active_tab": "homepage",
	}
	return render(request, "index.html", context)

def github(request):
	response = requests.get('https://api.github.com/users/gilliantrethewey/repos')
	repos = response.json()
	context = {
		"active_tab": "github",
		"github_repos": repos, 
	}
	return render(request, "github.html", context)

def about(request):
	context = {
		"active_tab": "about", 
	}
	return render(request, "about.html", context)

def blog_archive(request):
	context = {
		"active_tab": "blog_archive", 
	}
	return render(request, "blog-archive.html", context)

def portfolio(request):
	context = {
		"active_tab": "portfolio", 
	}
	return render(request, "portfolio.html", context)

def contact(request): 
	context = {
		"active_tab": "contact", 
	}
	return render(request, "contact.html", context)

def resume(request):
	context = {
		"active_tab": "resume", 
	}
	return render(request, "resume.html", context)

def services(request):
	context = {
		"active_tab": "services", 
	}
	return render(request, "services.html", context)

def blog_post_first(request):
	context = {
		"active_tab": "blog", 
	}
	return render(request, "blog-post-first.html", context)

def portfolio(request):
	context = {
		"active_tab": "portfolio", 
	}
	return render(request, "portfolio.html", context)

def portfolio_details_client_grid(request):
	context = {
		"active_tab": "portfolio", 
	}
	return render(request, "portfolio-details-client-grid.html", context)

def portfolio_details_feast_and_west(request): 
	context = {
		"active_tab": "portfolio", 
	}
	return render(request, "portfolio-details-feast-and-west.html", context)

def portfolio_details_github(request): 
	context = {
		"active_tab": "portfolio", 
	}
	return render(request, "portfolio-details-github.html", context)

def portfolio_details_kickstart_coding_data_project_2(request):
	context = {
		"active_tab": "portfolio", 
	}
	return render(request, "portfolio-details-kickstart-coding-data-project-2.html", context)

def portfolio_details_kickstart_coding_data_project_3(request):
	context = {
		"active_tab": "portfolio", 
	}
	return render(request, "portfolio-details-kickstart-coding-data-project-3.html", context)

def portfolio_details_peach_and_pine(request):
	context = {
		"active_tab": "portfolio", 
	}
	return render(request, "portfolio-details-peach-and-pine.html", context)

def portfolio_details_rachel_anzalone(request):
	context = {
		"active_tab": "portfolio", 
	}
	return render(request, "portfolio-details-rachel-anzalone.html", context)

def portfolio_details_shayla_boyd_gill(request): 
	context = {
		"active_tab": "portfolio", 
	}
	return render(request, "portfolio-details-shayla-boyd-gill.html", context)

def portfolio_details_west_trade(request): 
	context = {
		"active_tab": "portfolio", 
	}
	return render(request, "portfolio-details-west-trade.html", context)

