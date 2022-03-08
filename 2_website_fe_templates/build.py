from string import Template
global top_template, bottom_template
my_list_of_pages = [
    {
        'title': 'About',
        'input_file': 'content/about.html',
        'output_file': 'docs/about.html',
        'html_page': 'about_html',
        'sub_key': 'about_class'
    },
    {
        'title': 'Blog',
        'input_file': 'content/blog-archive.html',
        'output_file': 'docs/blog-archive.html',
        'html_page': 'blog_archive_html',
        'sub_key': 'blog_archive_class'
    },
    {
        'title': 'Blog',
        'input_file': 'content/blog-post-first.html',
        'output_file': 'docs/blog-post-first.html',
        'html_page': 'blog_post_first_html',
        'sub_key': 'blog_archive_class'
    },
    {
        'title': 'Contact',
        'input_file': 'content/contact.html',
        'output_file': 'docs/contact.html',
        'html_page': 'contact_html',
        'sub_key': 'contact_class'
    },
    {
        'title': 'Home',
        'input_file': 'content/index.html',
        'output_file': 'docs/index.html',
        'html_page': 'index_html',
        'sub_key': 'index_class'
    },
    {
        'title': 'Portfolio',
        'input_file': 'content/portfolio.html',
        'output_file': 'docs/portfolio.html',
        'html_page': 'portfolio_html',
        'sub_key': 'portfolio_class'
    },
    {
        'title': 'Resume',
        'input_file': 'content/resume.html',
        'output_file': 'docs/resume.html',
        'html_page': 'resume_html',
        'sub_key': 'resume_class'
    },
    {
        'title': 'Services',
        'input_file': 'content/services.html',
        'output_file': 'docs/services.html',
        'html_page': 'services_html',
        'sub_key': 'services_class'
    },
    {
        'title': 'Portfolio',
        'input_file': 'content/portfolio-details-client-grid.html',
        'output_file': 'docs/portfolio-details-client-grid.html',
        'html_page': 'portfolio_details_client_grid_html',
        'sub_key': 'portfolio_class'
    },
    {
        'title': 'Portfolio',
        'input_file': 'content/portfolio-details-feast-and-west.html',
        'output_file': 'docs/portfolio-details-feast-and-west.html',
        'html_page': 'portfolio_details_feast_and_west_html',
        'sub_key': 'portfolio_class'
    },
    {
        'title': 'Portfolio',
        'input_file': 'content/portfolio-details-github.html',
        'output_file': 'docs/portfolio-details-github.html',
        'html_page': 'portfolio_details_github_html',
        'sub_key': 'portfolio_class'
    },
    {
        'title': 'Portfolio',
        'input_file': 'content/portfolio-details-kickstart-coding-data-project-2.html',
        'output_file': 'docs/portfolio-details-kickstart-coding-data-project-2.html',
        'html_page': 'portfolio_details_kickstart_coding_data_project_2_html',
        'sub_key': 'portfolio_class'
    },
    {
        'title': 'Portfolio',
        'input_file': 'content/portfolio-details-kickstart-coding-data-project-3.html',
        'output_file': 'docs/portfolio-details-kickstart-coding-data-project-3.html',
        'html_page': 'portfolio_details_kickstart_coding_data_project_3_html',
        'sub_key': 'portfolio_class'
    },
    {
        'title': 'Portfolio',
        'input_file': 'content/portfolio-details-peach-and-pine.html',
        'output_file': 'docs/portfolio-details-peach-and-pine.html',
        'html_page': 'portfolio_details_peach_and_pine_html',
        'sub_key': 'portfolio_class'
    },
    {
        'title': 'Portfolio',
        'input_file': 'content/portfolio-details-rachel-anzalone.html',
        'output_file': 'docs/portfolio-details-rachel-anzalone.html',
        'html_page': 'portfolio_details_rachel_anzalone_html',
        'sub_key': 'portfolio_class'
    },
    {
        'title': 'Portfolio',
        'input_file': 'content/portfolio-details-shayla-boyd-gill.html',
        'output_file': 'docs/portfolio-details-shayla-boyd-gill.html',
        'html_page': 'portfolio_details_shayla_boyd_gill_html',
        'sub_key': 'portfolio_class'
    },
    {
        'title': 'Portfolio',
        'input_file': 'content/portfolio-details-west-trade.html',
        'output_file': 'docs/portfolio-details-west-trade.html',
        'html_page': 'portfolio_details_west_trade_html',
        'sub_key': 'portfolio_class'
    },
]

def template_read():
    #read in the top.html and bottom.html files 
    top_template = open('templates/top.html').read()
    bottom_template = open('templates/bottom.html').read()
    return top_template, bottom_template

def generate_pages(my_list_of_pages):
    top_template, bottom_template = template_read()
    #use my_list_of_pages to replace variables
    template = Template(top_template)
    for page in my_list_of_pages:
        temp_html = template.safe_substitute({
        'title': page['title'],
        page['sub_key']: 'active',
        })
        content = open(page['input_file']).read()
        page['html_page'] = temp_html + content + bottom_template
        open(page['output_file'], 'w+').write(page['html_page'])

def main(): # calls generate_pages, which calls template_read
    generate_pages(my_list_of_pages)

if __name__ == "__main__":
    main()