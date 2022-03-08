from django.shortcuts import render
from .models import DashboardPanel
import requests
import pygal

def home(request):
    context = {}
    return render(request, 'pages/home.html', context)

def graph(request):
    response = requests.get("https://api.github.com/users/GillianTrethewey/repos")
    repo_list = response.json()
    
    line_chart = pygal.Bar()
    line_chart.title = 'GitHub Repos by Size'
    for repo_stat in repo_list:
        size = repo_stat["size"]
        repo_name = repo_stat["name"]

        line_chart.add(repo_name,  size)

    context = {
        "github_repos": repo_list,
        "line_chart": line_chart.render().decode("utf8"),
    }

    return render(request, 'pages/graph.html', context)

def languages(request):
    response = requests.get("https://api.github.com/users/GillianTrethewey/repos")
    repo_list = response.json()
    
    pie_chart = pygal.Pie(inner_radius=.4)
    pie_chart.title = "Languages in GitHub Repos" 

    data = {}

    for repo_dict in repo_list:
        lang = repo_dict['language']
        if lang not in data:
            data[lang] = 0
        data[lang] += 1

    for lang, count in data.items():
        if not lang: continue
        pie_chart.add(lang,  count)

    context = {
        "github_repos": repo_list,
        "pie_chart": pie_chart.render().decode("utf8"),
    }

    return render(request, 'pages/languages.html', context)

def chart(request):
    response = requests.get("https://api.github.com/users/GillianTrethewey/repos")
    repo_list = response.json()
    
    context = {
        "github_repos": repo_list,
        }

    return render(request, 'pages/chart.html', context)

def home_panels(request):
    dboard_panels = DashboardPanel.objects.all()

    context = {
        "all_panels": dboard_panels,
    }

    return render(request, "pages/home_panels.html", context)

def panel_details(request, panel_id):
    panel = DashboardPanel.objects.get(id=panel_id)
    response = requests.get("https://api.github.com/users/GillianTrethewey/repos")
    repo_list = response.json()

    for item in repo_list:
        if panel.repo_name == item['name']:
            if panel.panel_type == "piechart":
                chart = pygal.Pie(inner_radius=.4)        
            else:
                chart = pygal.Bar()

            data = {}

            for repo_dict in repo_list:
                lang = repo_dict['language']
                if lang not in data:
                    data[lang] = 0
                data[lang] += 1

            for lang, count in data.items():
                if not lang: continue
                chart.add(lang, count)
            chart.title = "Coding Languages In " + panel.repo_name
        else:
            continue

    context = {
        "panel": panel,
        "rendered_chart_svg": chart.render().decode("utf8"),
    }

    return render(request, "pages/panel_details.html", context)
    