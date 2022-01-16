# Django Project

This is a lightweight and easy to setup boilerplate project for Django.

- Easy to setup
- Ready to start dev out of the box
- flexibility to rename
- and some awesome ✨Magic ✨

> Note: `./manage.py startapp <app-name>` Every time we create a new app, you will have to move it inside the apps package..

## Features

- All Apps managed and maintined under one folder.
- Settings are saperated in Base and Env with modular structure 
- Core APP responsible for:
    - Custom commands
    - Base setup
- Integrated Debug Toolbar
- Integrated Django REST framework
- Integrated Swagger
- Integrated Sentry 
- Integrated WKHTML 
- Integrated CORS 

## Tech

This project uses a number of open source projects to work properly:

- [Django] - Python web framework that encourages rapid development
- [Django Debug Toolbar] - configurable set of panels that display various debug information about the current request/response and when clicked, display more details about the panel's content.
- [Django REST framework] - Django REST framework is a powerful and flexible toolkit for building Web APIs.
- [Swagger] - Generate real Swagger/OpenAPI 2.0 specifications from a Django Rest Framework API.
- [Sentry] - Sentry's Django integration enables automatic reporting of errors and exceptions.
- [WKHTML] - Python 2 and 3 wrapper for wkhtmltopdf utility to convert HTML to PDF using Webkit.
- [CORS] - A Django App that adds Cross-Origin Resource Sharing (CORS) headers to responses. This allows in-browser requests to your Django application from other origins.

## Installation

> Note: Make sure you go through docs for `WKHTML` [here](https://pypi.org/project/pdfkit/)

> Utils: There are some common helpers available:
>> generate_pdf: Generated PDF object 
>> generate_csv: Generated CSV file object

Requires [Django] v4.0.1 to run.

Step 1 : Create Project root directory
```sh
mkdir <project_name> 
```

Step 2 : Clone the project in you <project_name> directory 
```sh
cd <project_name>
git clone https://github.com/abhi-tupparwar/django_project.git
```

Step 3 : Copy the contents of _config/settings/example.env.py_ to _config/settings/env.py_

Step 4 :Install the dependencies and start the server.

```sh
cd django_project
pip install -r requirements.txt // install requirements
./manage.py collectstatic //collect all static files
./manage.py runserver
```

To rename the project execute following command:
```sh
./manage.py rename_project <project_name> // renames django_project to specified project name
```

## Folder Structure
```
<project_name>
|
|---assets (folder created once static files are collected)
|
|---django_project
|   |---apps
|   |   |---core (core app)
|   |   |   |---utils.py
|   |   |---...<other apps>...
|   |   |---urls.py
|   |
|   |---config
|   |   |---settings
|   |   |   |---base.py
|   |   |   |---env.py
|   |   |   |---.env.sample
|   |   |   |---.env (ignored by git)
|   |   |
|   |   |---asgi.py
|   |   |---urls.py
|   |   |---wsgi.py
|   |   |---utils.py
|   |   |
|   |   |static_files (all static files we use in development)
|   |   |---base (project as a whole specific static files)
|   |   |   |---css
|   |   |   |---img
|   |   |   |---js
|   |   |---core (my custom app specific)
|   |   |   |---css
|   |   |   |---img
|   |   |   |---js
|   |   |
|   |---templates
|   |   |---core (custom app specific)
|   |   |---<other app specific templates>
|   |   |---base.html (included basics of jquery and bootstrap)
|   |
|   |---.gitignore
|   |---manage.py
|   |---requirements.txt
|   |---keys.py
|
|---media (folder created once items were uploaded)
|---db.sqlite3
```


## License

MIT

   [Django]: <https://www.djangoproject.com/>
   [Django REST framework]: <https://www.django-rest-framework.org/>
   [Swagger]: <https://drf-yasg.readthedocs.io/en/stable/readme.html>
   [Sentry]: <https://docs.sentry.io/platforms/python/guides/django/>
   [WKHTML]: <https://pypi.org/project/pdfkit/>
   [CORS]: <https://pypi.org/project/django-cors-headers/>
   [git-repo-url]: <https://github.com/abhi-tupparwar/django_project>
   [Django Debug Toolbar]: <https://django-debug-toolbar.readthedocs.io/en/latest/>
   
