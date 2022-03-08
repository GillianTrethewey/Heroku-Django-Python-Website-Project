import util
import sys

print('\nUsage:')
print('Rebuild site: python manage.py build')
print('Create new page: python manage.py new\n')
if len(sys.argv) > 1:
    command = sys.argv[1]
    if command == 'build':
        print('Build was specified')
        util.dict_populate()
        util.generate_pages()
    elif command == 'new':
        print('New page was specified')
        util.new_page()
    else:
        print("Please specify 'build' or 'new'")
    
else:
    print("Invalid command: please select 'build' or 'new'")