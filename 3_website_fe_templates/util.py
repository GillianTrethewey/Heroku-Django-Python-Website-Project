import glob
import os
import requests
from jinja2 import Template
pages = []
str_pages = ''

all_html_files = glob.glob("content/*.html")

def dict_populate():
	for file_path in all_html_files:
		file_name = os.path.basename(file_path)
		name_only, extension = os.path.splitext(file_name)
		content_path = "content/" + file_name
		output_path = "docs/" + file_name
		pages.append({
    		"filename": file_path,
    		"title": name_only,
    		"input_file": content_path,
    		"output_file": output_path,
		})


def generate_pages():
	for page in pages:
		content_html = open(page['input_file']).read()
		template_html = open('templates/base.html').read()
		template = Template(template_html)
		context = {
			'pages': pages,
			'content': content_html,
			'title': page['title'],
			}
		
		output = template.render(context)

		open(page['output_file'], 'w+').write(output)

def new_page():
    open('content/new-content-page.html', "w+").write('<h1>New Content Page</h1><p>New Content</p>')
