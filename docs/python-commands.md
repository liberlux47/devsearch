# Python and Django Essential Commands Guide

## Python Basics

### Running Python Scripts
```bash
# Run a Python script
python script.py

# Run Python interactively
python

# Run a one-line Python command
python -c "print('Hello, World!')"
```

## Python Virtual Environments

### Creating Virtual Environments
```bash
# Create a virtual environment
python -m venv env

# Create with specific Python version
python3.10 -m venv env
```

### Activating Virtual Environments
```bash
# On Windows
env\Scripts\activate

# On macOS/Linux
source env/bin/activate
```

### Deactivating Virtual Environments
```bash
# Works the same on all platforms
deactivate
```

### Managing Packages
```bash
# Install packages
pip install package_name

# Install specific version
pip install package_name==1.2.3

# Install from requirements file
pip install -r requirements.txt

# List installed packages
pip list

# Generate requirements file
pip freeze > requirements.txt
```

## Django Commands

### Installation
```bash
# Install Django
pip install django

# Install specific version
pip install django==4.2.1
```

### Project Setup
```bash
# Create new Django project
django-admin startproject project_name

# Create new app within a project
python manage.py startapp app_name
```

### Database Commands
```bash
# Create database migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser for admin
python manage.py createsuperuser
```

### Running the Development Server
```bash
# Run development server
python manage.py runserver

# Run on specific port
python manage.py runserver 8080
```

### Django Shell
```bash
# Open Django interactive shell
python manage.py shell
```

### Static Files and Testing
```bash
# Collect static files
python manage.py collectstatic

# Run tests
python manage.py test
```

### Other Useful Django Commands
```bash
# Check for problems in your project
python manage.py check

# List all available commands
python manage.py help
```

## Django App Development

### Generating New Django Apps
```bash
# Create a new app
python manage.py startapp app_name

# Create app within a specific directory
python manage.py startapp app_name path/to/directory

# Create app with custom template
python manage.py startapp --template=path/to/template app_name
```

### Registering Apps
After creating a new app, you need to "register" it with your project to make Django aware of it. This process involves adding the app to the `INSTALLED_APPS` list in your project's `settings.py` file.:
```python
INSTALLED_APPS = [
    # Django built-in apps
    'django.contrib.admin',
    'django.contrib.auth',
    # ...
    
    # Your custom apps
    'app_name/apps/[AppConfigFile]',
]
```
#### Why Register Apps?
- **Discovery**: Django needs to know which apps to include when running commands like migrations or collecting static files
- **Template Loading**: Django searches for templates within registered apps
- **Admin Integration**: Registered apps can have their models appear in the admin interface
- **URL Configuration**: Makes it easier to include app-specific URLs in the project's URL patterns
- **Static Files**: Django will look for static files in registered apps when using `collectstatic` command

#### When to Register Apps
Always register your app immediately after creating it, before attempting to:
- Create or run migrations
- Use the app's models in your project
- Access the app's templates or static files
- Include the app's URLs in your project's URL configuration

Without proper registration, Django will not recognize your app's components as part of the project.

## Django App Structure

### Key Files and Folders in a Django App
```
app_name/
├── migrations/         # Database migration files
├── __init__.py         # Makes the directory a Python package
├── admin.py            # Admin interface configuration
├── apps.py             # App configuration
├── models.py           # Database models (i.e. database schemas)
├── tests.py            # Test functions
├── urls.py             # URL routing for the app (may need to create)
└── views.py            # View functions/classes
```

### Common Additional Files
```
app_name/
├── forms.py            # Form classes
├── signals.py          # Custom signals
├── middleware.py       # Custom middleware
├── managers.py         # Custom model managers
├── templatetags/       # Custom template tags
│   └── app_filters.py
├── static/             # Static files (CSS, JS, images)
└── templates/          # HTML templates
    └── app_name/       # App-specific templates
```

### Purpose of Key Files

- **migrations/**: Contains database changes that Django uses to update your database schema
- **admin.py**: Register models to appear in the Django admin interface
- **apps.py**: Contains app configuration class
- **models.py**: Define database models using Django's ORM
- **tests.py**: Write tests for your application
- **urls.py**: Define URL patterns specific to the app
- **views.py**: Handle requests and return responses